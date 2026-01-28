'''
API endpoints for managing teams.

'''
from fastapi import APIRouter
from data.teams import ALL_TEAMS, Team, TeamModel
from data.drivers import DriverModel
from data.stats import StatsModel
from fastapi import HTTPException
import logging

logging.basicConfig(level=logging.DEBUG)

teams_router = APIRouter()

#converting to json for the frontend
@teams_router.get("/teams", response_model=list[TeamModel])
def get_all_teams():
    """
    this endpoint returns a list of all teams.
    """
    try:
        teams = [
            TeamModel(
                **{key: value for key, value in vars(team).items() if key != "drivers"},
                drivers=[
                    DriverModel(
                        **{key: value for key, value in vars(driver).items() if key != "stats"},
                        stats=StatsModel(**vars(driver.stats))
                    ).dict()
                    for driver in team.drivers
                ]
            )
            for team in ALL_TEAMS.values()
        ]
        logging.debug("Teams data serialized successfully: %s", teams)
        return teams
    except Exception as e:
        logging.error("Error retrieving teams: %s", e)
        raise HTTPException(status_code=500, detail=str(e))



#getting a single team by name
@teams_router.get("/teams/{team_name}", response_model=TeamModel)
def get_team(team_name: str):
    """
    this endpoint returns a single team by name.
    """
    team_name = team_name.lower()  #need to normalize
    team = ALL_TEAMS.get(team_name)
    if not team:
         raise HTTPException(status_code=404, detail="Team not found")
    
    return TeamModel(**vars(team))