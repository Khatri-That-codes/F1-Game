'''
This file is for managing driver statistics in the racing simulation game.
'''

#making an enum for stats to maintain consistency
from enum import Enum

class Stat(Enum):
    WINS = "total_wins"
    PODIUMS = "total_podiums"
    POLES = "total_poles"
    DNFS = "total_dnfs"
    POINTS = "total_points"


class Stats:
    def __init__(self):
        self.total_wins = 0
        self.total_podiums = 0
        self.total_poles = 0
        self.total_dnfs = 0
        self.total_points = 0

    def record_race(self, wins: int, podiums: int, poles: int, dnfs: int, points: int):
        """Update stats after a race."""            
        self.total_wins += wins
        self.total_podiums += podiums
        self.total_poles += poles
        self.total_dnfs += dnfs
        self.total_points += points

    def update_stat(self, stat: Stat, value: int):
        """Update a specific stat."""
        if hasattr(self, stat.value):
            setattr(self, stat.value, getattr(self, stat.value) + value)
        