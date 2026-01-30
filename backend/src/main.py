from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from api.drivers import drivers_router
from api.teams import teams_router
from api.tracks import tracks_router
from api.standings import standings_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True, 
)


# Api routers
app.include_router(drivers_router, prefix="/api")
app.include_router(teams_router, prefix="/api")
app.include_router(tracks_router, prefix="/api")
app.include_router(standings_router)