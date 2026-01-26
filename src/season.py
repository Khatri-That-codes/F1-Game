'''
This file maanges the season class and it functions
'''
from src.race_engine import RaceEngine
from src.models import Driver, Track
from typing import List
import random
import json

class Season:
    def __init__(self, drivers: List[Driver], tracks: List[Track]):
        self.drivers = drivers
        self.tracks = tracks
        self.current_round = 0
        self.standings = {d.name: 0 for d in drivers}


    def run_next_race(self):
        track = self.tracks[self.current_round]
        weather = "Rain" if random.random() < track.weather_bias else "Dry"


        engine = RaceEngine(self.drivers, track, weather)
        results = engine.run_race()


        points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
        for i, driver in enumerate(results[:10]):
            self.standings[driver.name] += points[i]
            driver.xp += 2


        self.current_round += 1
        return results, engine.commentary_log, engine.incidents
    

    def is_season_complete(self):
        return self.current_round >= len(self.tracks)
    
    def save_game(self, filename):
        """Save the current season state to a JSON file."""
        data = {
            "current_round": self.current_round,
            "standings": self.standings,
            "drivers": [driver.to_dict() for driver in self.drivers],
            "tracks": [track.to_dict() for track in self.tracks]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_game(cls, filename):
        """Load a season state from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)

        drivers = [Driver.from_dict(d) for d in data["drivers"]]
        tracks = [Track.from_dict(t) for t in data["tracks"]]
        season = cls(drivers, tracks)
        season.current_round = data["current_round"]
        season.standings = data["standings"]
        return season





## testing 

if __name__ == "__main__":
    drivers = [
            Driver("Verstappen", "Red Bull", skill=95, aggression=70),
            Driver("Hamilton", "Mercedes", skill=90, aggression=60),
            Driver("Leclerc", "Ferrari", skill=88, aggression=65),
        ]

    tracks = [
    Track("Monza", difficulty=60, weather_bias=0.2),
    Track("Silverstone", difficulty=55, weather_bias=0.4),
    ]


    season = Season(drivers, tracks)


    results, commentary, incidents = season.run_next_race()


    print("Race Commentary:")
    for line in commentary:
        print(line)


    print("Final Results:")
    for i, d in enumerate(results, start=1):
        print(f"{i}. {d.name}")


    print("Season Standings:")
    for k, v in season.standings.items():
        print(k, v)

    # Save the game
    season.save_game("season_save.json")

    # Load the game
    loaded_season = Season.load_game("season_save.json")
    print("Loaded Season Standings:", loaded_season.standings)