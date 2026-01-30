import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { Button, Card } from "../components/UIComponents";
import { useTheme } from "../context/ThemeContext";

const RaceIntroScreen = () => {
  const { theme } = useTheme();
  const location = useLocation();
  const navigate = useNavigate();
  const { selectedTrack } = location.state || {};

  if (!selectedTrack) {
    return (
      <div
        style={{
          backgroundColor: theme.backgroundColor,
          color: theme.textColor,
          minHeight: "100vh",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <h1 style={{ color: theme.primaryColor }}>Race Intro</h1>
        <p>No track selected. Please go back and select a track.</p>
        <Button onClick={() => navigate("/track-select")}>Go Back</Button>
      </div>
    );
  }

  return (
    <div
      style={{
        backgroundColor: theme.backgroundColor,
        color: theme.textColor,
        minHeight: "100vh",
        padding: "40px 20px",
        fontFamily: '"Press Start 2P", Arial, sans-serif',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center'
      }}
    >
      <h1 style={{ 
        color: theme.primaryColor, 
        marginBottom: '40px',
        fontSize: '2.5rem',
        textAlign: 'center' 
      }}>Race Introduction</h1>

      <Card style={{
        backgroundColor: theme.cardBackground,
        border: `3px solid ${theme.primaryColor}`,
        borderRadius: '20px',
        padding: '40px',
        maxWidth: '600px',
        width: '100%',
        textAlign: 'center',
        boxShadow: `0 10px 20px ${theme.cardShadow}`
      }}>
        <h2>Track: {selectedTrack.name}</h2>
        <img
          src={selectedTrack.image}
          alt={selectedTrack.name}
          style={{ width: "100%", borderRadius: "10px" }}
        />
        <p>
          <strong>Location:</strong> {selectedTrack.location}
        </p>
        <p>
          <strong>Length:</strong> {selectedTrack.length} km
        </p>
      </Card>

      <div style={{ marginTop: "20px" }}>
        <Button onClick={() => navigate("/race")}>Start Race</Button>
      </div>
    </div>
  );
};

export default RaceIntroScreen;