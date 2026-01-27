"""
Module for managing the season calendar.
"""

from typing import List
from data.tracks import ALL_TRACKS

# Placeholder season calendar
SEASON_CALENDAR: List = list(ALL_TRACKS.values())

def get_next_race(current_index: int) -> str:
    """Get the next race in the calendar."""
    if current_index + 1 < len(SEASON_CALENDAR):
        return SEASON_CALENDAR[current_index + 1]
    return "End of Season"

def get_current_race(current_index: int) -> str:
    """Get the current race in the calendar."""
    return SEASON_CALENDAR[current_index]

def reset_season() -> int:
    """Reset the season to the first race."""
    return 0