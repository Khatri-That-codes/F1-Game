'''
This file manages player class, its attributes and methods
'''

from src.team import Team

class Player:
    def __init__(self, name: str, racing_team: Team = None):
        '''
        Team will be default None if not provided in the constructor
        '''
        self.name = name
        self.racing_team = racing_team

        #adding to the racing team
        if racing_team:
            racing_team.players.append(self)

        self.XP = 0  # Experience points

    def add_xp(self, points: int):
        '''
        This method adds experience points to the player
        Parameters:
        points - number of points to be added
        '''
        self.XP += points


    def __str__(self):
        return f"Player: {self.name}, Team: {self.racing_team.name}, XP: {self.XP}"
    

    def to_json(self) -> dict:
        '''
        Method to convert the Player object to a JSON dictionary.
        Returns:
            dict: A dictionary representation of the Player object.
        '''
        return {
            "name": self.name,
            "racing_team": self.racing_team.to_json(),
            "XP": self.XP
        }
    
    @staticmethod
    def load_player_from_json(data: dict, team: str) -> 'Player':
        '''
        Static method to create a Player object from a JSON dictionary.

        Requires the team list to be available to scan for existing teams.
        Parameters:
            data (dict): A dictionary containing player data.
            team (str): Team name of the player.
            Player: An instance of the Player class.

        
        '''

        name = data.get("name", "Unknown Player")
        team_name = team if team != "" else None
        racing_team = None

        for team in Team.team_list:
            if team.name == team_name:
                racing_team = team
                break 
            

        if team_name != "" and racing_team is None:
            racing_team = Team(team_name)   
        
        xp = data.get("XP", 0)
        player = Player(name, racing_team)
        player.XP = xp
        return player
    
    
    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return (self.name == other.name and
                self.racing_team == other.racing_team and
                self.XP == other.XP)