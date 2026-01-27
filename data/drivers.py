'''
This file manages driver data for the racing simulation game.
'''

from typing import Dict, Any
from teams import ALL_TEAMS, Team
from stats import Stats

class Driver:
    def __init__(self, name: str, team: Team, number: int, nation: str,  qualifying: int, aggression: int):
        self.name = name
        self.team = team
        self.team_name = team.name
        self.number = number
        self.nation = nation  # need to decide if this is emoji or name of country
        self.xp = 0 #starting with zero
        self.qualifying = qualifying  # for the qualifying position?
        
        self.isActive = True 
        self.aggression = aggression


        # need to add check for this part. replace with generic image if not found
        self.driver_image = f"assets/drivers/{self.name.lower().replace(' ', '_')}.png"
    
        
        # need to see this part
        self.stats: Stats = Stats()



    def add_xp(self, amount: int):
        """Add experience points to the driver."""
        self.xp += amount

    def update_qualifying(self, new_qualifying: int):
        """Update the driver's qualifying stat."""
        self.qualifying = new_qualifying




#ALL the drivers in the game

ALL_DRIVERS: Dict[str, Driver] = {
    "max_verstappen": Driver("Max Verstappen", ALL_TEAMS["red_bull"], 33, "Netherlands", 95, 90),
    "daniel_ricciardo": Driver("Daniel Ricciardo", ALL_TEAMS["red_bull"], 3, "Australia", 88, 78),
    "george_russell": Driver("George Russell", ALL_TEAMS["mercedes"], 63, "UK", 87, 77),
    "lewis_hamilton": Driver("Lewis Hamilton", ALL_TEAMS["mercedes"], 44, "UK", 93, 85),
    "charles_leclerc": Driver("Charles Leclerc", ALL_TEAMS["ferrari"], 16, "Monaco", 92, 80),
    "lando_norris": Driver("Lando Norris", ALL_TEAMS["mclaren"], 4, "UK", 89, 75),
    "oscar_piastri": Driver("Oscar Piastri", ALL_TEAMS["mclaren"], 81, "Australia", 84, 72),

    "lance_stroll": Driver("Lance Stroll", ALL_TEAMS["aston_martin"], 18, "Canada", 85, 70),
      
    "carlos_sainz": Driver("Carlos Sainz", ALL_TEAMS["ferrari"], 55, "Spain", 86, 74),

    # need to add alpine, sauber drivers 
    
}