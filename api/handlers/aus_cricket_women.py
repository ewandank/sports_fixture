from hishel.httpx import AsyncCacheClient

from enums import Teams
from registry import register_option
from utils.cricket import get_fixture_params, parse_fixture_response


@register_option(Teams.AUS_CRICKET_WOMEN)
async def get_fixure(client: AsyncCacheClient):
    raw_fixtures = (
        (
            await client.get(
                "https://apiv2.cricket.com.au/web/fixtures/yearfilter?",
                params=get_fixture_params(68),
            )
        )
        .raise_for_status()
        .json()
    )
    return parse_fixture_response(raw_fixtures, include_game_str=True)
