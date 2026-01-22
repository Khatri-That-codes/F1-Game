'''
This file maages the stewards , and approach to an incident
'''

from src.models import Incident
import random

class Stewards:


    @staticmethod
    def review_incident(incident: Incident) -> Incident:
        roll = random.randint(1, 100)


        if incident.severity > 70 and roll > 30:
            incident.penalty = "10s Time Penalty"
            incident.driver.stats["penalties"] += 1
        elif incident.severity > 40 and roll > 60:
            incident.penalty = "5s Time Penalty"
            incident.driver.stats["penalties"] += 1
        else:
            incident.penalty = "No Further Action"


        return incident