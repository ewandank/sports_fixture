from ics.event import Event
from hishel.httpx import AsyncCacheClient

from enums import Teams
from registry import register_option
from utils.cricket import fetch_team_fixtures,



@register_option(Teams.AUS_CRICKET_WOMEN)
async def get_fixture(client: AsyncCacheClient):
    return fetch_team_fixtures(client, team_id=68)