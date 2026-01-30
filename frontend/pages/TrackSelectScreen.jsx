import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { fetchTracks } from "../api";
import { Button, Card } from "../components/UIComponents";
import { useTheme } from "../context/ThemeContext";

const TrackSelectScreen = () => {
  const { theme } = useTheme();
  const [tracks, setTracks] = useState([]);
  const [selectedTrack, setSelectedTrack] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetchTracks()
      .then((data) => setTracks(data))
      .catch((error) => console.error("Error fetching tracks:", error));
  }, []);

  const handleTrackSelect = (event) => {
    const trackName = event.target.value;
    const track = tracks.find((t) => t.name === trackName);
    setSelectedTrack(track);
  };

  const handleProceedToIntro = () => {
    if (!selectedTrack) {
      alert("Please select a track first!");
      return;
    }

    navigate("/race-intro", { state: { selectedTrack } });
  };

  return (
    <div
      style={{
        backgroundColor: theme.backgroundColor,
        color: theme.textColor,
        minHeight: "100vh",
        padding: "20px",
      }}
    >
      <h1 style={{ color: theme.primaryColor, marginTop: "30px" }}>
        Select a Track
      </h1>

      <Card>
        <label htmlFor="track-select">Select a Track:</label>
        <select
          id="track-select"
          onChange={handleTrackSelect}
          style={{ margin: "10px 0" }}
        >
          <option value="">--Choose a Track--</option>
          {tracks.map((track) => (
            <option key={track.id} value={track.name}>
              {track.name}
            </option>
          ))}
        </select>
      </Card>

      <div style={{ marginTop: "20px" }}>
        <Button onClick={handleProceedToIntro}>Proceed to Race Intro</Button>
      </div>
    </div>
  );
};

export default TrackSelectScreen;