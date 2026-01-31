"""
Module for managing track data.
"""

from typing import Dict, List
from data.weather import WEATHER_CONDITION, WeatherModel
from enum import Enum
from pydantic import BaseModel

class Track:
    def __init__(self, name: str, country: str, number_laps: int,  weather_options: WEATHER_CONDITION):
        self.name = name
        self.country = country
        self.number_laps = number_laps
        self.weather_options = weather_options

      #neeed to addd check to replace with generic image if not found 
        self.image_path = f"/images/tracks/{self.name.lower().replace(' ', '_')}.png"






ALL_TRACKS: Dict[str, Track] = {
    "suzuka": Track("Suzuka", "Japan", 53, [WEATHER_CONDITION.SUNNY, WEATHER_CONDITION.RAINY]),
    "monza": Track("Monza", "Italy", 53, [WEATHER_CONDITION.SUNNY, WEATHER_CONDITION.CLOUDY]),
    "spa" : Track("Spa", "Belgium", 44, [WEATHER_CONDITION.RAINY, WEATHER_CONDITION.CLOUDY]),
    "monaco": Track("Monaco", "Monaco", 78, [WEATHER_CONDITION.SUNNY, WEATHER_CONDITION.STORMY]),
    "silverstone": Track("Silverstone", "UK", 52, [WEATHER_CONDITION.SUNNY, WEATHER_CONDITION.CLOUDY]),

    "generic track": Track("Generic Track", "Nowhere", 50, [WEATHER_CONDITION.SUNNY, WEATHER_CONDITION.RAINY, WEATHER_CONDITION.CLOUDY, WEATHER_CONDITION.STORMY])
}


class TrackModel(BaseModel):
    name: str
    country: str
    number_laps: int
    weather_options: List[WeatherModel]  # Updated to use WeatherModel
    image_path: str