'''
File for location related classes and functions.

'''

class Location:
    '''
    Class representing a location in the F1 game.
    Attributes:
        name (str): The name of the location.
        country (str): The country where the location is situated.
        track_length_km (float): The length of the track in kilometers.
    '''
    def __init__(self, name: str, country: str, number_laps: int):
        self.name = name
        self.country = country
        self.number_laps = number_laps

    
    def __str__(self):
        return f"{self.name}, {self.country} - {self.number_laps} laps"
    

    @staticmethod
    def load_loc_from_json(data: dict) -> 'Location':
        '''
        Static method to create a Location object from a JSON dictionary.
        Parameters:
            data (dict): A dictionary containing location data.
        Returns:
            Location: An instance of the Location class.
        '''
        name = data.get("name", "Unknown Location")
        country = data.get("country", "Unknown Country")
        number_laps = data.get("number_laps", 0)
    

        return Location(name, country, number_laps)
    


    def to_json(self) -> dict:
        '''
        Method to convert the Location object to a JSON dictionary.
        Returns:
            dict: A dictionary representation of the Location object.
        '''
        return {
            "name": self.name,
            "country": self.country,
            "number_laps": self.number_laps
        }


    
    def __eq__(self, other):
        if not isinstance(other, Location):
            return False
        return (self.name == other.name and
                self.country == other.country and
                self.number_laps == other.number_laps)
    

    