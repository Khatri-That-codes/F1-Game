'''
This file handles the Team class, its attributes and methods
'''

class Team:

    team_list = []  
    def __init__(self, name: str):
        self.name = name
        self.team_points = 0  # Total points for the team
        self.players = []  # List to hold players in the  - empty initially

        Team.team_list.append(self)

    def add_team_points(self, points: int):
        '''
        This method adds points to the team's total points
        Parameters:
        points - number of points to be added
        '''
        self.team_points += points

    def __str__(self):
        return f"Team: {self.name}, Points: {self.team_points}"
    
    def to_json(self) -> dict:
        '''
        Method to convert the Team object to a JSON dictionary.
        Returns:
            dict: A dictionary representation of the Team object.
        '''
        return {
            "name": self.name,
            "team_points": self.team_points
        }
    
    @staticmethod
    def load_team_from_json(data: dict) -> 'Team':
        '''
        Static method to create a Team object from a JSON dictionary.
        Parameters:
            data (dict): A dictionary containing team data.
        Returns:
            Team: An instance of the Team class.                                
        '''
        name = data.get("name", "Unknown Team")
        team_points = data.get("team_points", 0)
        team = Team(name)
        team.team_points = team_points
        return team