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
        backgroundImage: `url('/public/images/ui/f1_track_background.jpg')`,
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
      // style={{
      //   backgroundColor: theme.backgroundColor,
      //   color: theme.textColor,
      //   minHeight: "100vh",
      //   padding: "40px 20px",
      //   fontFamily: '"Press Start 2P", Arial, sans-serif',
      //   display: 'flex',
      //   flexDirection: 'column',
      //   alignItems: 'center',
      //   justifyContent: 'center'
      // }}
    >
      {/* <h1 style={{ 
        color: theme.primaryColor, 
        marginBottom: '40px',
        fontSize: '2.5rem',
        textAlign: 'center' 
      }}>Race Introduction</h1> */}

      <Card style={{
        backgroundColor: "rgba(103, 33, 33, 0.8)",
        // backgroundColor: theme.cardBackground,
        border: `3px solid ${theme.primaryColor}`,
        borderRadius: '20px',
        padding: '20px',
        maxWidth: '400px',
        width: '100%',
        textAlign: 'center',
        boxShadow: `0 10px 20px ${theme.cardShadow}`
      }}>
        <p>Track: {selectedTrack.name}</p>
        <img
          src={selectedTrack.image_path}
          alt={selectedTrack.name}
          style={{ width: "100%", borderRadius: "10px" , maxWidth: '250px', margin: '20px 0'}}
        />
        <p>
          <strong>Location:</strong> {selectedTrack.country}
        </p>
        <p>
          <strong>Number of Laps:</strong> {selectedTrack.number_laps}
        </p>
      </Card>

      <div style={{ marginTop: "20px" }}>
        <Button onClick={() => navigate("/race", { state: { selectedTrack } })}>Start Race</Button>
      </div>
    </div>
  );
};

export default RaceIntroScreen;