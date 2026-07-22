from enum import IntFlag, auto
from fastapi import FastAPI
from utils import from_base58_num

app = FastAPI()

# This can in theory expand indefinitely whilst keeping older ones compliant as the bits won't change. 
class Options(IntFlag):
    AUS_CRICKET_MEN = auto()
    AUS_CRICKET_WOMEN = auto()
    STARS_AFLM = auto()
    STARS_AFLW = auto()
    DEMONS_AFLM = auto()
    DEMONS_AFLW = auto()
    MELB_UNITED = auto()


@app.get("/v1/fixture/{fixture_base64_bitmask}")
def get_fixtures(b58_mask):
    foo = Options(from_base58_num(b58_mask))
    print(f"{foo!r}")
    return {"decoded":f"{foo!r}"}
