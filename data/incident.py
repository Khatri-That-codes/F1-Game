"""
this file manages incidents

"""
from dataclasses import dataclass
from enum import Enum
from data.drivers import ALL_DRIVERS, Driver
import random


@dataclass
class Incident:
    driver: Driver
    description: str
    severity: int # 1–100
    penalty: str = None


class IncidentType(Enum):
    COLLISION = "Collision"
    UNSAFE_RELEASE = "Unsafe Release"
    MECHANICAL_FAILURE = "Mechanical Failure"
    OTHER = "Other"


#this function will make an incident randomly for a driver
def generate_random_incident():
    driver = random.choice(list(ALL_DRIVERS.values()))
    incident_type = random.choice(list(IncidentType))
    severity = random.randint(1, 100)

    descriptions = {
        IncidentType.COLLISION: f"{driver.name} was involved in a collision.",
        IncidentType.UNSAFE_RELEASE: f"{driver.name} had an unsafe release from the pit lane.",
        IncidentType.MECHANICAL_FAILURE: f"{driver.name} suffered a mechanical failure.",
        IncidentType.OTHER: f"{driver.name} encountered an unexpected issue.",
    }

    description = descriptions[incident_type]
    penalty = "Drive-through penalty" if severity > 70 else None

    return Incident(driver=driver, description=description, severity=severity, penalty=penalty)




