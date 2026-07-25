import arrow
from hishel.httpx import AsyncCacheClient
from ics.event import Event

COMMON_PARAMS = {"isCompleted": False, "jsconfig": "elun", "format": "json"}
BASE_URL = "https://apiv2.cricket.com.au/web"


async def fetch_team_fixtures(
    client: AsyncCacheClient,
    team_id: int,
    competition_id: int | None = None,
    include_game_str: bool = False,
) -> list[Event]:
    params = {
        "teamId": team_id,
        "limit": 100,
        "isInningInclude": True,
        **COMMON_PARAMS,
    }
    if competition_id is not None:
        params["competitionId"] = competition_id

    res = await client.get(f"{BASE_URL}/fixtures/yearfilter", params=params)
    res.raise_for_status()

    events = []
    for fixture in res.json().get("fixtures") or []:
        home = fixture.get("home_team").get("name", "")
        away = fixture.get("away_team").get("name", "")
        clean_home = home.removesuffix("Women").removesuffix("Men").strip()
        match_str = f"{clean_home} vs {away}"

        e = Event()
        e.name = (
            f"{match_str} - {fixture.get('name')}" if include_game_str else match_str
        )
        e.uid = str(fixture.get("id"))
        e.begin = fixture.get("start_date_time")
        e.end = fixture.get("end_date_time")
        e.location = fixture.get("venue").get("name")
        events.append(e)

    return events


async def get_competition_id(
    client: AsyncCacheClient, team_id: int, str_match: str
) -> int | None:
    response = await client.get(
        f"{BASE_URL}/competitions/format/year",
        params={
            "teamId": team_id,
            "limit": 50,
            "year": str(arrow.utcnow().year),
            **COMMON_PARAMS,
        },
    )

    response.raise_for_status()

    for details in response.json().get("competition_details"):
        if str_match in details.get("name"):
            return details.get("competition_id")
    return None
