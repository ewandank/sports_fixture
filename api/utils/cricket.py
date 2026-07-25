import arrow
from ics.event import Event


def parse_fixture_response(response, include_game_str=False) -> list[Event]:
    events: list[Event] = []
    for fixture in response.get("fixtures"):
        e = Event()
        e.name = _get_event_name(
            home_team_name=fixture.get("home_team").get("name"),
            away_team_name=fixture.get("away_team").get("name"),
            game_name=fixture.get("name"),
            include_game_str=include_game_str,
        )
        e.uid = str(fixture.get("id"))
        e.begin = fixture.get("start_date_time")
        e.end = fixture.get("start_date_time")
        e.location = fixture.get("venue").get("name")
        events.append(e)
    return events


def _get_event_name(
    home_team_name: str, away_team_name: str, game_name: str, include_game_str=False
) -> str:
    home_team_name_clean = (
        home_team_name.removesuffix("Women").removesuffix("Men").strip()
    )
    # e.g. Australia vs England Women - 1st ODI
    if include_game_str:
        return f"{home_team_name_clean} vs {away_team_name} - {game_name}"
    else:
        return f"{home_team_name_clean} vs {away_team_name}"


def get_fixture_params(team_id: int, competition_id=None):
    return {
        "teamId": team_id,
        **({"competitionId": competition_id} if competition_id is not None else {}),
        "limit": 100,
        "isInningInclude": True,
        **_common_params,
    }


def get_competition_params(team_id: int):
    return {
        "teamId": team_id,
        "limit": 50,
        "year": str(arrow.utcnow().year),
        **_common_params,
    }


_common_params = {
    "isCompleted": False,
    "jsconfig": "elun",
    "format": "json",
}


def get_competition_id(response, str_match):
    for details in response.get("competition_details"):
        if str_match in details.get("name"):
            return details.get("competition_id")
