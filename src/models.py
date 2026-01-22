'''
This file includes data models for the racing simulation game.
'''
import random
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Driver:
    name: str
    team: str
    xp: int = 0
    skill: int = 50
    aggression: int = 50 
    stats: dict = field(default_factory=lambda: {
    "wins": 0,
    "podiums": 0,
    "dnf": 0,
    "penalties": 0,
    "races": 0
    })




@dataclass
class Team:
    name: str
    car_performance: int 




@dataclass
class Track:
    name: str
    difficulty: int
    weather_bias: float # chance of rain





# incidents to which the stewards may react

@dataclass
class Incident:
    driver: Driver
    description: str
    severity: int # 1–100
    penalty: Optional[str] = None


