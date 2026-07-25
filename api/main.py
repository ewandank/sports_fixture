from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from hishel import AsyncSqliteStorage
from hishel.httpx import AsyncCacheClient
from ics import Calendar
from ics.event import Event

# side effect imports are "magical"
import handlers  # noqa: F401
from enums import Teams
from registry import registry
from utils.base58 import from_base58_num


@asynccontextmanager
async def lifespan(app: FastAPI):
    storage = AsyncSqliteStorage(database_path="cache.sqlite", default_ttl=14400)
    app.state.http_client = AsyncCacheClient(storage=storage)
    yield
    await app.state.http_client.aclose()


app = FastAPI(lifespan=lifespan)


def get_client(request: Request) -> AsyncCacheClient:
    return request.app.state.http_client


class CalendarResponse(Response):
    media_type = "text/calendar"


@app.get("/v1/fixture", response_class=CalendarResponse)
async def v1_get_fixtures(
    b58_mask: str,
    client: Annotated[AsyncCacheClient, Depends(get_client)],
):
    try:
        requested_teams = Teams(from_base58_num(b58_mask))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid calendar options")
    calendar_items: list[Event] = await registry.get_combined_data(
        requested_teams, client
    )
    # TODO: metadata
    c = Calendar()

    c.events.update(calendar_items)
    return c.serialize()
