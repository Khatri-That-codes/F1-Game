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
        padding: "20px",
      }}
    >
      <h1 style={{ color: theme.primaryColor }}>Race Introduction</h1>

      <Card>
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