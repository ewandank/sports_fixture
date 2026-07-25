from enum import CONFORM, IntFlag, auto


# This can in theory expand indefinitely whilst keeping older ones compliant as the bits won't change.
# conform means it strips any bits outside of the accepted values.
class Teams(IntFlag, boundary=CONFORM):
    AUS_CRICKET_MEN = auto()
    AUS_CRICKET_WOMEN = auto()
    STARS_BBL = auto()
    STARS_WBBL = auto()
    DEMONS_AFL = auto()
    DEMONS_AFLW = auto()
    MELB_UNITED = auto()
