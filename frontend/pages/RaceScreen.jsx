import React, { useState, useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { fetchTracks, fetchDrivers } from "../api"; // Import centralized API functions
import { Button, Card } from "../components/UIComponents";
import { useTheme } from "../context/ThemeContext";

const RaceScreen = () => {
  const { theme } = useTheme();
  const location = useLocation();
  const navigate = useNavigate();
  const { selectedTrack, drivers } = location.state || {};

  if (!selectedTrack || !drivers) {
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
        <h1 style={{ color: theme.primaryColor }}>Race Screen</h1>
        <p>No track or drivers selected. Please go back and select a track.</p>
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
      <h1 style={{ color: theme.primaryColor, marginTop: "30px" }}>Race Screen</h1>

      <Card>
        <h2>Track: {selectedTrack.name}</h2>
        <p>
          <strong>Location:</strong> {selectedTrack.location}
        </p>
        <p>
          <strong>Length:</strong> {selectedTrack.length} km
        </p>
      </Card>

      <div style={{ marginTop: "20px" }}>
        <Button onClick={() => navigate("/race-intro")}>Back to Intro</Button>
      </div>
    </div>
  );
};

export default RaceScreen;