'''
API endpoints for managing drivers.
'''

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
    return [DriverModel(**vars(driver)) for driver in ALL_DRIVERS.values()]



#gettgin a single driver by name
@drivers_router.get("/drivers/{driver_name}", response_model=DriverModel)
def get_driver(driver_name: str):
    """
    this endpoint returns a single driver by name.
    """
    driver_name = driver_name.lower()  #need to normalize
    driver = ALL_DRIVERS.get(driver_name)
    if not driver:
         raise HTTPException(status_code=404, detail="Driver not found")
    
    return DriverModel(**vars(driver))



#get driver's stats by driver name
@drivers_router.get("/drivers/{driver_name}/stats", response_model=StatsModel)
def get_driver_stats(driver_name: str):
    """
    this endpoint returns a driver's stats by name.
    """
    driver_name = driver_name.lower()  #need to normalize
    driver = ALL_DRIVERS.get(driver_name)
    if not driver:
         raise HTTPException(status_code=404, detail="Driver not found")
    
    return StatsModel(**vars(driver.stats))