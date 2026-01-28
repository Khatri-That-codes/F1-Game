'''
manages the api endpoints for the race
'''

from typing import List
from fastapi import APIRouter, HTTPException
from backend.data.drivers import Driver, ALL_DRIVERS, DriverModel
from backend.data.tracks import Track, ALL_TRACKS, TrackModel

from src.race_engine import RaceEngine
from backend.data.race import Race, RaceModel
from fastapi import WebSocket, WebSocketDisconnect


race_router = APIRouter()


@race_router.post("/race/start")
def start_race(track_name: str):
    """
    Stimulates the qualifying session, finals and reurns the results.
    """

    track_name = track_name.lower() #for consistency

    track : Track = ALL_TRACKS.get(track_name)

    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    

    race = Race(list(ALL_DRIVERS.values()), track, track.weather)

    qualifying  = race.simulate_qualifying()
    final = race.simulate_final_race()

    return {
        "qualifying_results": [driver.name for driver in qualifying["results"]],
        "qualifying_commentary": qualifying["commentary"],
        "final_results": [driver.name for driver in final["results"]],
        "final_commentary": final["commentary"]
    }




@race_router.websocket("/race/live")
async def live_race(websocket: WebSocket, track_name: str):
    """
    Streams real-time commentary during the race.
    """
    await websocket.accept()

    track = ALL_TRACKS.get(track_name.lower())
    if not track:
        await websocket.send_json({"error": "Track not found"})
        await websocket.close()
        return

    race = Race(list(ALL_DRIVERS.values()), track, track.weather)

    try:
        # Use the run_race_with_animation function to send updates
        def update_ui_callback(commentary):
            websocket.send_json({"commentary": commentary})

        race.engine.run_race_with_animation(update_ui_callback)
        await websocket.send_json({"status": "Race Finished!"})
    except WebSocketDisconnect:
        print("WebSocket disconnected")