from hishel.httpx import AsyncCacheClient

from enums import Teams
from registry import register_option
from utils.cricket import (
    get_competition_id,
    get_competition_params,
    get_fixture_params,
    parse_fixture_response,
)


@register_option(Teams.STARS_WBBL)
async def get_fixure(client: AsyncCacheClient):

    team_id = 97

    competition_response = (
        (
            await client.get(
                "https://apiv2.cricket.com.au/web/competitions/format/year",
                params=get_competition_params(team_id),
            )
        )
        .raise_for_status()
        .json()
    )
    competition_id = get_competition_id(competition_response, "WBBL")

    raw_fixtures = (
        (
            await client.get(
                "https://apiv2.cricket.com.au/web/fixtures/yearfilter?",
                params=get_fixture_params(team_id, competition_id),
            )
        )
        .raise_for_status()
        .json()
    )
    return parse_fixture_response(raw_fixtures)
