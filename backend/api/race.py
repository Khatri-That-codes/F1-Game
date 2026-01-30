'''
manages the api endpoints for the race
'''

from typing import List
from fastapi import APIRouter, HTTPException
from backend.data.drivers import Driver, ALL_DRIVERS, DriverModel
from backend.data.tracks import Track, ALL_TRACKS, TrackModel
from fastapi import WebSocket, WebSocketDisconnect
import logging
from backend.data.race import Race

logging.basicConfig(level=logging.INFO)

race_router = APIRouter()


@race_router.post("/race/start")
def start_race(track_name: str):
    """
    Stimulates the qualifying session, finals and returns the results.
    """

    track_name = track_name.lower()  # for consistency
    logging.info(f"Received track_name: {track_name}")

    track: Track = ALL_TRACKS.get(track_name)

    if not track:
        logging.error(f"Track not found: {track_name}")
        raise HTTPException(status_code=404, detail="Track not found")

    race = Race(list(ALL_DRIVERS.values()), track, track.weather)

    qualifying = race.simulate_qualifying()
    final = race.simulate_final_race()

    return {
        "qualifying_results": [driver.name for driver in qualifying["results"]],
        "qualifying_commentary": qualifying["commentary"],
        "final_results": [driver.name for driver in final["results"]],
        "final_commentary": final["commentary"],
    }


@race_router.post("/race/commentary")
def get_race_commentary(track_name: str):
    """
    Simulates the race and returns commentary updates and results.
    """
    track_name = track_name.lower()
    logging.info(f"Received track_name: {track_name}")

    track = ALL_TRACKS.get(track_name)
    if not track:
        logging.error(f"Track not found: {track_name}")
        raise HTTPException(status_code=404, detail="Track not found")

    race = Race(list(ALL_DRIVERS.values()), track, track.weather)

    # Simulate the race
    qualifying = race.simulate_qualifying()
    final = race.simulate_final_race()

    return {
        "qualifying_results": [driver.name for driver in qualifying["results"]],
        "qualifying_commentary": qualifying["commentary"],
        "final_results": [driver.name for driver in final["results"]],
        "final_commentary": final["commentary"],
    }


@race_router.websocket("/race/live")
async def live_race(websocket: WebSocket):
    """
    Streams real-time commentary during the race.
    """
    # Extract track_name from query parameters
    track_name = websocket.query_params.get("track_name")
    if not track_name:
        logging.error("Missing track_name in query parameters")
        await websocket.accept()
        await websocket.send_json({"error": "Missing track_name in query parameters"})
        await websocket.close()
        return

    logging.info(f"Received track_name: {track_name}")

    await websocket.accept()

    track = ALL_TRACKS.get(track_name.lower())
    if not track:
        logging.error(f"Track not found: {track_name}")
        await websocket.send_json({"error": "Track not found"})
        await websocket.close()
        return

    logging.info(f"Track found: {track.name}")

    race = Race(list(ALL_DRIVERS.values()), track, track.weather)

    try:
        # Use the run_race_with_animation function to send updates
        async def update_ui_callback(commentary):
            await websocket.send_json({"commentary": commentary})

        race.engine.run_race_with_animation(update_ui_callback)
        await websocket.send_json({"status": "Race Finished!"})
    except WebSocketDisconnect:
        logging.warning("WebSocket disconnected")