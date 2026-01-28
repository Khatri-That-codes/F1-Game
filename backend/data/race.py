'''
manages a race instance
'''
from typing import List
from backend.data.drivers import Driver
from backend.data.tracks import Track
from backend.data.weather import WEATHER_CONDITION
from src.race_engine import RaceEngine
from pydantic import BaseModel

class Race:
    def __init__(self, drivers: List[Driver], track: Track, weather: WEATHER_CONDITION):
        self.drivers = drivers
        self.track = track
        self.weather = weather
        self.engine: RaceEngine = RaceEngine(drivers, track, weather)

    def simulate_qualifying(self) -> dict:
        """
        Simulates the qualifying session and returns the grid order.
        """
        return {
            "results": self.engine.qualify(),
            "commentary": self.engine.commentary_log
        }

    def simulate_final_race(self) -> dict:
        """
        Simulates the final race and returns the race results.
        """
        return {
            "results": self.engine.run_race(),
            "commentary": self.engine.commentary_log,
        }
    


class RaceModel(BaseModel):
    drivers: List[Driver]
    track: Track
    weather: WEATHER_CONDITION
