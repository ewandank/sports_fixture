from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Request
from hishel import AsyncSqliteStorage
from hishel.httpx import AsyncCacheClient

from enums import Teams
from registry import registry
from utils import from_base58_num
# side effect imports are "magically"
import handlers  # noqa: F401

storage = AsyncSqliteStorage(connection="cache.sqlite", default_ttl=14400)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http_client = AsyncCacheClient(storage=storage)
    yield
    await app.state.http_client.aclose()


app = FastAPI(lifespan=lifespan)


def get_client(request: Request) -> AsyncCacheClient:
    return request.app.state.http_client


@app.get("/v1/fixture/{fixture_base64_bitmask}")
async def v1_get_fixtures(
    b58_mask: str, client: AsyncCacheClient = Depends(get_client)
):
    try:
        requested_teams = Teams(from_base58_num(b58_mask))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid calendar options")
    calendar_items = await registry.get_combined_data(requested_teams, client)
    return calendar_items
