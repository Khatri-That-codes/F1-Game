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
        backgroundImage: `url('/assets/images/ui/f1_track_background.jpg')`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        minHeight: "100vh",
        padding: "40px 20px",
        fontFamily: '"Press Start 2P", Arial, sans-serif',
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center"
      }}
    >
      {/* <h1 style={{ 
        color: theme.primaryColor, 
        marginBottom: "40px",
        textAlign: 'center',
        fontSize: '2.5rem'
      }}>
        Select a Track
      </h1> */}

      <Card style={{
        backgroundColor: "rgba(255, 255, 255, 0.8)",
        border: `3px solid ${theme.primaryColor}`,
        borderRadius: '20px',
        padding: '40px',
        maxWidth: '500px',
        width: '100%',
        textAlign: 'center',
        boxShadow: `0 10px 20px ${theme.cardShadow}`
      }}>
        <label htmlFor="track-select" style={{ 
          fontSize: '1.2rem', 
          marginBottom: '20px',
          display: 'block',
          color: theme.primaryColor
        }}>Select a Track:</label>
        <select
          id="track-select"
          onChange={handleTrackSelect}
          style={{ 
            margin: "20px 0",
            padding: '15px 20px',
            fontSize: '1rem',
            borderRadius: '10px',
            border: `2px solid ${theme.primaryColor}`,
            backgroundColor:  theme.backgroundColor,
            color: theme.textColor,
            fontFamily: '"Press Start 2P", Arial, sans-serif',
            width: '100%',
            maxWidth: '300px'
          }}
        >
          <option value="">Choose a Track</option>
          {tracks.map((track) => (
            <option key={track.id} value={track.name}>
              {track.name}
            </option>
          ))}
        </select>
      </Card>

      <div style={{ marginTop: "40px" }}>
        <Button style={{
          backgroundColor: theme.primaryColor,
          color: theme.textColor,
          fontSize: '1.1rem',
          padding: '15px 30px',
          borderRadius: '10px',
          border: 'none'
        }} onClick={handleProceedToIntro}>Proceed to Race Intro</Button>
      </div>
    </div>
  );
};

export default TrackSelectScreen;