from hishel.httpx import AsyncCacheClient

from enums import Teams
from registry import register_option
from utils.cricket import fetch_team_fixtures, get_competition_id


@register_option(Teams.STARS_WBBL)
async def get_fixture(client: AsyncCacheClient):
    team_id = 97
    competition_id = await get_competition_id(client, team_id, "WBBL")
    return fetch_team_fixtures(client, team_id, competition_id)
