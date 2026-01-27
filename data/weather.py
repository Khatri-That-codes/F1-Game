"""
manages weather data for the racing simulation game.
"""

from enum import Enum
from typing import List, Dict

class Weather:

    def __init__(self, condition: str, temperature: float, difficulty_factor: float):
        self.condition = condition 
        self.temperature = temperature 
        self.difficulty_factor = difficulty_factor  



class WEATHER_CONDITION(Enum):
    SUNNY = Weather("Sunny", 30.0, 1.0)
    RAINY = Weather("Rainy", 20.0, 1.5)
    CLOUDY = Weather("Cloudy", 25.0, 1.2)
    STORMY = Weather("Stormy", 18.0, 2.0)

