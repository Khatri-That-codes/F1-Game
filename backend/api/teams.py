'''
API endpoints for managing teams.

'''
from fastapi import APIRouter
from data.teams import ALL_TEAMS, Team
from fastapi import HTTPException


teams_router = APIRouter()

#converting to json for the frontend
@teams_router.get("/teams", response_model=list[Team])
def get_all_teams():
    """
    this endpoint returns a list of all teams.
    """
    return list(ALL_TEAMS.values())



#getting a single team by name
@teams_router.get("/teams/{team_name}", response_model=Team)
def get_team(team_name: str):
    """
    this endpoint returns a single team by name.
    """
    team_name = team_name.lower()  #need to normalize
    team = ALL_TEAMS.get(team_name)
    if not team:
         raise HTTPException(status_code=404, detail="Team not found")
    return team