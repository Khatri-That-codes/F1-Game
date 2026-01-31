import React, { useState, useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { Button, Card } from "../components/UIComponents";
import { useTheme } from "../context/ThemeContext";

const RaceScreen = () => {
  const { theme } = useTheme();
  const location = useLocation();
  const navigate = useNavigate();
  const { selectedTrack } = location.state || {};

  const [commentaryLog, setCommentaryLog] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!selectedTrack) {
      navigate("/race-intro");
      return;
    }

    const hardcodedData = {
      qualifying_commentary: [
        "Qualifying session begins!",
        "Driver A sets the fastest lap!",
        "Driver B spins out in sector 2!",
        "Qualifying session ends!",
      ],
      final_commentary: [
        "The race starts!",
        "Driver A takes the lead!",
        "Driver C overtakes Driver B!",
        "Driver A wins the race!",
      ],
      final_results: ["Driver A", "Driver C", "Driver B"],
    };

    setCommentaryLog([...hardcodedData.qualifying_commentary, ...hardcodedData.final_commentary]);
    setLoading(false);
  }, [selectedTrack, navigate]);

  const handleResultsClick = () => {
    navigate("/results", {
      state: {
        raceResults: ["Driver A", "Driver C", "Driver B"],
      },
    });
  };

  return (
    <div
      style={{
        backgroundColor: theme.backgroundColor,
        color: theme.textColor,
        minHeight: "100vh",
        padding: "40px 20px",
        fontFamily: '"Press Start 2P", Arial, sans-serif',
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <h1
        style={{
          color: theme.primaryColor,
          marginBottom: "40px",
          fontSize: "2.5rem",
          textAlign: "center",
        }}
      >
        Race in Progress
      </h1>

      {loading && <p>Loading race commentary...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      <div style={{ display: "flex", gap: "10px", marginBottom: "20px" }}>
        {["black", "black", "black", "black", "black"].map((color, index) => (
          <div
            key={index}
            style={{
              width: "30px",
              height: "30px",
              borderRadius: "50%",
              backgroundColor: color,
            }}
          ></div>
        ))}
      </div>

      <div
        style={{
          backgroundColor: theme.cardBackground,
          border: `3px solid ${theme.primaryColor}`,
          borderRadius: "20px",
          padding: "20px",
          maxWidth: "600px",
          width: "100%",
          textAlign: "left",
          boxShadow: `0 10px 20px ${theme.cardShadow}`,
          overflowY: "auto",
          maxHeight: "400px",
          marginBottom: "20px",
        }}
      >
        {commentaryLog.map((comment, index) => (
          <p key={index} style={{ margin: "10px 0" }}>
            {comment}
          </p>
        ))}
      </div>

      <Button
        onClick={handleResultsClick}
        style={{
          marginTop: "20px",
          padding: "10px 20px",
          fontSize: "1rem",
          backgroundColor: theme.primaryColor,
          color: theme.textColor,
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
      >
        Go to Results
      </Button>
    </div>
  );
};

export default RaceScreen;