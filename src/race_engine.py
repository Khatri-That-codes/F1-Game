'''
This file manages the game engine 
'''
import random
from src.models import Driver, Track, Incident

from src.stewards import Stewards
from typing import List

from src.dialogues import Dialogues

class RaceEngine:


    
    def __init__(self, drivers: List[Driver], track: Track, weather: str):
        self.drivers = drivers
        self.track = track
        self.weather = weather
        self.incidents: List[Incident] = []
        self.commentary_log: List[str] = []

    def qualify(self) -> List[Driver]:
        """
        Qualifying influenced by XP, skill, and randomness
        Uses aux function quali_score to calculate score for sorting
        """

        def quali_score(driver):
            return (
            driver.skill
            + driver.xp * 0.2
            + random.randint(-15, 15)
            )


        return sorted(self.drivers, key=quali_score, reverse=True)


    def maybe_incident(self, driver: Driver):
        '''
        Calculates a chance and hence if an incident occurs or not
        '''
        chance = driver.aggression + self.track.difficulty
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
            driver.skill
            + driver.xp * 0.3
            + random.randint(-20, 20)
            )


            if self.weather == "Rain":
                base -= random.randint(0, 10)


            self.maybe_incident(driver)
            results.append((base, driver))


        results.sort(key=lambda x: x[0], reverse=True)
        final_order = [d for _, d in results]


        self.update_stats(final_order)

        self.commentary_log.append(Dialogues.get_random_event_commentary("FINISH"))
        return final_order




    def update_stats(self, order: List[Driver]):
        for i, driver in enumerate(order):
            driver.stats["races"] += 1


            if i == 0:
                driver.stats["wins"] += 1
            if i < 3:
                driver.stats["podiums"] += 1




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