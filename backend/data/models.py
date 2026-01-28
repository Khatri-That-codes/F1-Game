from pydantic import BaseModel
from typing import Any
from data.stats import StatsModel

class DriverModel(BaseModel):
    name: str
    team_name: str
    number: int
    nation: str
    xp: int
    qualifying: int
    aggression: int
    isActive: bool
    driver_image: str
    stats: StatsModel