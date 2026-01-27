"""
This file manages all the team data for the racing simulation game.
"""

from typing import Dict
from theme import TEAM_COLORS

class Team:
    def __init__(self, name: str, logo_path: str, team_colour: str):
        self.name = name
        self.logo_path = logo_path
        self.team_colour = team_colour
        self.team_points = 0 #initialing team points to 0
        

# Placeholder data for teams
ALL_TEAMS: Dict[str, Team] = {
    "alpine": Team("Alpine", "assets/teams/alpine.png", TEAM_COLORS["alpine"]),
    "ferrari": Team("Ferrari", "assets/teams/ferrari.png", TEAM_COLORS["ferrari"]), 
    "mclaren": Team("McLaren", "assets/teams/mclaren.png", TEAM_COLORS["mclaren"]),
    "mercedes": Team("Mercedes", "assets/teams/mercedes.png", TEAM_COLORS["mercedes"]),
    "red_bull": Team("Red Bull", "assets/teams/red_bull.png", TEAM_COLORS["red_bull"]),
    "aston_martin": Team("Aston Martin", "assets/teams/aston_martin.png", TEAM_COLORS["aston_martin"]),
    "williams": Team("Williams", "assets/teams/williams.png", TEAM_COLORS["williams"]),
    "sauber": Team("Sauber", "assets/teams/sauber.png", TEAM_COLORS["sauber"])
}