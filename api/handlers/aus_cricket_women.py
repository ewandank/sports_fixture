from hishel.httpx import AsyncCacheClient

from enums import Teams
from registry import register_option


@register_option(Teams.AUS_CRICKET_WOMEN)
async def get_fixure(client: AsyncCacheClient):
    # TODO: Implement me properly
    return ["hello"]
