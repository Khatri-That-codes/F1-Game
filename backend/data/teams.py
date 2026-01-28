"""
This file manages all the team data for the racing simulation game.
"""

from typing import Dict
from theme.colour_palette import TEAM_COLORS

class Team:
    def __init__(self, name: str, team_colour: str):
        self.name = name
        
        self.team_colour = team_colour
        self.team_points = 0 #initialing team points to 0
        self.logo_path = f"assets/images/teams/{self.name.lower().replace(' ', '_')}.png"

# Placeholder data for teams
ALL_TEAMS: Dict[str, Team] = {
    "alpine": Team("Alpine", TEAM_COLORS["alpine"]),
    "ferrari": Team("Ferrari",  TEAM_COLORS["ferrari"]), 
    "mclaren": Team("McLaren", TEAM_COLORS["mclaren"]),
    "mercedes": Team("Mercedes", TEAM_COLORS["mercedes"]),
    "red_bull": Team("Red Bull", TEAM_COLORS["red_bull"]),
    "aston_martin": Team("Aston Martin", TEAM_COLORS["aston_martin"]),
    "williams": Team("Williams", TEAM_COLORS["williams"]),
    "sauber": Team("Sauber",  TEAM_COLORS["sauber"])
}