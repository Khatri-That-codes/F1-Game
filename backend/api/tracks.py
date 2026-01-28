'''
API endpoints for managing tracks
'''

from fastapi import APIRouter
from data.tracks import ALL_TRACKS, Track, TrackModel
from fastapi import HTTPException

tracks_router = APIRouter()

#converting to json for the frontend
@tracks_router.get("/tracks", response_model=list[TrackModel])
def get_all_tracks():
    """
    this endpoint returns a list of all tracks.
    """
    return [
        TrackModel(
            name=track.name,
            country=track.country,
            number_laps=track.number_laps,
            weather_options=[condition.to_model() for condition in track.weather_options],
            image_path=track.image_path
        )
        for track in ALL_TRACKS.values()
    ]


#getting a single track by track name
@tracks_router.get("/tracks/{track_name}", response_model=TrackModel)
def get_track(track_name: str):
    """
    this endpoint returns a single track by name.
    """
    track_name = track_name.lower()  #need to normalize
    track = ALL_TRACKS.get(track_name)
    if not track:
         raise HTTPException(status_code=404, detail="Track not found")
    
    return TrackModel(
        name=track.name,
        country=track.country,
        number_laps=track.number_laps,
        weather_options=[condition.to_model() for condition in track.weather_options],
        image_path=track.image_path
    )