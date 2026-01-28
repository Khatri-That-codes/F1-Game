from fastapi import APIRouter, HTTPException
from data.teams import ALL_TEAMS, TeamModel
from data.stats import StatsModel

standings_router = APIRouter()

@standings_router.get("/api/standings", response_model=list[TeamModel])
def get_team_standings():
    """
    This endpoint returns the team standings based on team points.
    """
    try:
        # Sort teams by points in descending order
        sorted_teams = sorted(ALL_TEAMS.values(), key=lambda team: team.team_points, reverse=True)
        return [
            TeamModel(
                name=team.name,
                team_colour=team.team_colour,
                team_points=team.team_points,
                logo_path=team.logo_path,
                base=team.base,
                principal=team.principal,
                championships=team.championships,
                drivers=[
                    {
                        "name": driver.name,
                        "team_name": driver.team_name,
                        "number": driver.number,
                        "nation": driver.nation,
                        "xp": driver.xp,
                        "qualifying": driver.qualifying,
                        "aggression": driver.aggression,
                        "isActive": driver.isActive,
                        "driver_image": driver.driver_image,
                        "stats": StatsModel(
                            total_wins=driver.stats.total_wins,
                            total_podiums=driver.stats.total_podiums,
                            total_poles=driver.stats.total_poles,
                            total_dnfs=driver.stats.total_dnfs,
                            total_points=driver.stats.total_points
                        ).dict()
                    }
                    for driver in team.drivers
                ]
            )
            for team in sorted_teams
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving standings: {e}")