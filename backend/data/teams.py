"""
This file manages all the team data for the racing simulation game.
"""

from typing import Dict, List, Optional
from theme.colour_palette import TEAM_COLORS
from data.drivers import Driver

class Team:
    def __init__(self, name: str, team_colour: str, base: str, principal: str, championships: int = 0, drivers: Optional[List[Driver]] = None):
        self.name = name
        self.team_colour = team_colour
        self.team_points = 0  
        self.logo_path = f"assets/images/teams/{self.name.lower().replace(' ', '_')}.png"
        self.base = base 
        self.principal = principal  
        self.championships = championships  
        self.drivers = drivers if drivers else []  

# Updating placeholder data for teams
ALL_TEAMS: Dict[str, Team] = {
    "alpine": Team("Alpine", TEAM_COLORS["alpine"], "Enstone, UK", "Otmar Szafnauer", 0),
    "ferrari": Team("Ferrari", TEAM_COLORS["ferrari"], "Maranello, Italy", "Fred Vasseur", 16),
    "mclaren": Team("McLaren", TEAM_COLORS["mclaren"], "Woking, UK", "Andrea Stella", 8),
    "mercedes": Team("Mercedes", TEAM_COLORS["mercedes"], "Brackley, UK", "Toto Wolff", 8),
    "red_bull": Team("Red Bull", TEAM_COLORS["red_bull"], "Milton Keynes, UK", "Christian Horner", 5),
    "aston_martin": Team("Aston Martin", TEAM_COLORS["aston_martin"], "Silverstone, UK", "Mike Krack", 0),
    "williams": Team("Williams", TEAM_COLORS["williams"], "Grove, UK", "James Vowles", 9),
    "sauber": Team("Sauber", TEAM_COLORS["sauber"], "Hinwil, Switzerland", "Alessandro Alunni Bravi", 0)
}