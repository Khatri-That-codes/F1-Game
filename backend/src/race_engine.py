'''
This file manages the game engine 
'''
import random
from data.incident import Incident
from data.stewards import Stewards
from data.drivers import Driver
from data.tracks import Track
from data.weather import WEATHER_CONDITION, Weather

from typing import List

from data.dialogues import Dialogues
from data.weather import WEATHER_CONDITION, Weather

class RaceEngine:

    def __init__(self, drivers: List[Driver], track: Track, weather: WEATHER_CONDITION):
        self.drivers = drivers
        self.track = track
        self.weather = weather.value
        self.incidents: List[Incident] = []
        self.commentary_log: List[str] = []

    def qualify(self) -> List[Driver]:
        """
        Qualifying influenced by XP, skill, and randomness
        Uses aux function quali_score to calculate score for sorting

        Returns a list of drivers sorted by qualifying performance
        """

        def quali_score(driver: Driver) -> float:
            return (
            driver.aggression  #need to decide if aggression affects qualifying or change to skill
            + driver.xp * 0.2 #might need to remove magic number
            + random.randint(-15, 15)  # positive or negative randomness allows more variability
            )

        return sorted(self.drivers, key=quali_score, reverse=True)


    def maybe_incident(self, driver: Driver):
        '''
        Calculates a chance and hence if an incident occurs or not
        '''
        chance = driver.aggression  + (self.weather.difficulty_factor * 10) 
        roll = random.randint(1, 200)


        if roll < chance:
            severity = random.randint(20, 100)
            incident = Incident(
            driver=driver,
            description=f"Incident involving {driver.name}",
            severity=severity
            )
            reviewed_incident = Stewards.review_incident(incident)
            self.incidents.append(reviewed_incident)

            self.commentary_log.append(Dialogues.get_random_event_commentary("INCIDENT"))

            self.commentary_log.append(
            f"{driver.name} had an incident! Severity: {severity}"
            f"Stewards decision: {reviewed_incident.penalty}"
            )


    def run_race(self) -> List[Driver]:
        """Simulates the race result"""

        self.commentary_log.append(Dialogues.get_random_event_commentary("START"))

        results = []


        for driver in self.drivers:
            base = (
            driver.aggression
            + driver.xp * 0.3 
            + random.randint(-20, 20)
            )


            if self.weather == WEATHER_CONDITION.RAINY:
                base -= random.randint(0, 10)


            self.maybe_incident(driver)
            results.append((base, driver))


        results.sort(key=lambda x: x[0], reverse=True)
        final_order = [d for _, d in results]



        self.commentary_log.append(Dialogues.get_random_event_commentary("FINISH"))
        return final_order




    def run_race_with_animation(self, update_ui_callback):
        """Simulates the race with periodic updates to the UI."""
        import time

        self.commentary_log.append(Dialogues.get_random_event_commentary("START"))
        update_ui_callback("Race Start!")
        time.sleep(1)  # Simulate delay for race start

        results = []

        for driver in self.drivers:
            base = (
                driver.skill
                + driver.xp * 0.3
                + random.randint(-20, 20)
            )

            if self.weather == WEATHER_CONDITION.RAINY:
                base -= random.randint(0, 10)

            self.maybe_incident(driver)
            results.append((base, driver))

            # Update UI with commentary
            update_ui_callback(self.commentary_log[-1])
            time.sleep(0.5)  # Simulate delay for each driver

        results.sort(key=lambda x: x[0], reverse=True)
        final_order = [d for _, d in results]

        self.update_stats(final_order)

        self.commentary_log.append(Dialogues.get_random_event_commentary("FINISH"))
        update_ui_callback("Race Finished!")
        return final_order




#Test code



if __name__ == "__main__":
    drivers = [
    Driver("Verstappen", "Red Bull", skill=95, aggression=70),
    Driver("Hamilton", "Mercedes", skill=90, aggression=60),
    Driver("Leclerc", "Ferrari", skill=88, aggression=65),
    ]


    track = Track("Monza", difficulty=60, weather_bias=0.2)


    engine = RaceEngine(drivers, track, weather="Dry")
    grid = engine.qualify()
    results = engine.run_race()


    print("Final Results:")
    for i, d in enumerate(results, start=1):
        print(f"{i}. {d.name}")


    print("\nIncidents:")
    for inc in engine.incidents:
        print(f"{inc.description} → {inc.penalty}")