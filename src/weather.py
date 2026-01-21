'''
Class for managing weather conditions in the F1 game.
'''

class Weather:
    def __init__(self, condition: str, temperature_celsius: float, humidity_percent: float):
        self.condition = condition  # e.g., "Sunny", "Rainy", "Cloudy"
        self.temperature_celsius = temperature_celsius
        self.humidity_percent = humidity_percent

    
    def __str__(self):
        return f"Weather: {self.condition}, Temp: {self.temperature_celsius}°C, Humidity: {self.humidity_percent}%"
    

    def to_json(self) -> dict:
        '''
        Method to convert the Weather object to a JSON dictionary.
        Returns:
            dict: A dictionary representation of the Weather object.
        '''
        return {
            "condition": self.condition,
            "temperature_celsius": self.temperature_celsius,
            "humidity_percent": self.humidity_percent
        }
    

    @staticmethod
    def load_weather_from_json(data: dict) -> 'Weather':
        '''
        Static method to create a Weather object from a JSON dictionary.
        Parameters:
            data (dict): A dictionary containing weather data.
        Returns:

            Weather: An instance of the Weather class.
    
        '''

        condition = data.get("condition", "Unknown")
        temperature_celsius = data.get("temperature_celsius", 0.0)
        humidity_percent = data.get("humidity_percent", 0.0)
        return Weather(condition, temperature_celsius, humidity_percent)
    


