import React from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "../components/UIComponents";
import { useTheme } from "../context/ThemeContext";

const MainMenu = () => {
  const navigate = useNavigate();
  const { theme } = useTheme();

  const styles = {
    container: {
      position: "relative",
      minHeight: "100vh",
      overflow: "hidden",
      display: "flex",
      alignItems: "flex-end", 
      justifyContent: "center",
      paddingBottom: "10px", 
    },
    video: {
      position: "absolute",
      top: 0,
      left: 0,
      width: "100%",
      height: "100%",
      objectFit: "cover",
      zIndex: -1,
    },
    card: {
      position: "relative",
      backgroundColor: theme.cardBackground,
      color: theme.textColor,
      padding: "20px",
      borderRadius: "10px",
      boxShadow: "0 4px 8px rgba(0, 0, 0, 0.2)",
      textAlign: "center",
      zIndex: 1,
      width: "650px",
      border: `2px solid ${theme.primaryColor}`,
      fontFamily: "'Press Start 2P', cursive", /* Retro font */
    },
    title: {
      fontSize: "1.5rem",
      color: theme.primaryColor,
      marginBottom: "20px",
      textShadow: "2px 2px 5px rgba(0, 0, 0, 0.5)",
    },
  };

  return (
    <div style={styles.container}>
      <video style={styles.video} autoPlay loop muted>
        <source src="assets/videos/f1_video.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>

      <div style={styles.card}>
        {/* <h1 style={styles.title}>F1 Racing Game</h1> */}

        <div style={{ display: "flex", flexDirection: "row", gap: "10px" }}>
          <Button onClick={() => navigate("/track-select")}>Start Race</Button>
          <Button onClick={() => navigate("/drivers")}>View Drivers</Button>
          <Button onClick={() => navigate("/teams")}>View Teams</Button>
          <Button onClick={() => navigate("/standings")}>View Standings</Button>
        </div>
      </div>
    </div>
  );
};

export default MainMenu;