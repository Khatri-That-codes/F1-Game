'''
API endpoints for managing drivers.
'''

from urllib.parse import unquote
from fastapi import APIRouter
from data.drivers import ALL_DRIVERS, Driver, DriverModel
from data.stats import StatsModel
from fastapi import HTTPException


drivers_router = APIRouter()

#converting to json for the frontend
@drivers_router.get("/drivers", response_model=list[DriverModel])
def get_all_drivers():
    """
    this endpoint returns a list of all drivers.
    """
    return [
        DriverModel(
            **{key: value for key, value in vars(driver).items() if key != "stats"},
            stats=StatsModel(
                total_wins=driver.stats.total_wins,
                total_podiums=driver.stats.total_podiums,
                total_poles=driver.stats.total_poles,
                total_dnfs=driver.stats.total_dnfs,
                total_points=driver.stats.total_points
            )
        )
        for driver in ALL_DRIVERS.values()
    ]



@drivers_router.get("/drivers/{driver_name}", response_model=DriverModel)
def get_driver(driver_name: str):
    """
    This endpoint returns a single driver by name.
    """
    driver_name = unquote(driver_name)
    driver_name = driver_name.lower().replace(" ", "_")
    driver = ALL_DRIVERS.get(driver_name)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")

    # Convert stats to StatsModel
    stats_model = StatsModel(
        total_wins=driver.stats.total_wins,
        total_podiums=driver.stats.total_podiums,
        total_poles=driver.stats.total_poles,
        total_dnfs=driver.stats.total_dnfs,
        total_points=driver.stats.total_points,
    )

    return DriverModel(**{key: value for key, value in vars(driver).items() if key != "stats"}, stats=stats_model)


#get driver's stats by driver name
@drivers_router.get("/drivers/{driver_name}/stats", response_model=StatsModel)
def get_driver_stats(driver_name: str):
    """
    this endpoint returns a driver's stats by name.
    """
    driver_name = unquote(driver_name)
    driver_name = driver_name.lower().replace(" ","_")
    driver = ALL_DRIVERS.get(driver_name)
    if not driver:
         raise HTTPException(status_code=404, detail="Driver not found")
    
    return StatsModel(**vars(driver.stats))