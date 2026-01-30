import React from "react";
import { useTheme } from "../context/ThemeContext";
import "../theme.css";

const TopBar = () => {
  const { theme } = useTheme();

  const styles = {
    container: {
      display: "flex",
      alignItems: "center",
      justifyContent: "start", 
      gap: "10px", 
      padding: "10px 20px",
      backgroundColor:  "rgba(135, 9, 9, 0.8)",//theme.cardBackground,
      color: "rgba(255, 255, 255, 0.9)",
      boxShadow: "0 4px 8px rgba(135, 9, 9, 0.2)",
      position: "fixed",
      top: 0,
      width: "100%",
      zIndex: 1000,
    },
    logo: {
      height: "30px",
      marginRight: "5px", 
    },
    title: {
      fontSize: "1.5rem",
      fontFamily: "'Press Start 2P',Arial, sans-serif", // Retro font with fallback
      color: "rgba(255, 255, 255, 0.9)",
    },
  };

  return (
    <div style={styles.container}>
      <img src="assets/images/ui/f1_logo.png" alt="F1 Logo" style={styles.logo} />
      <span style={styles.title}>F1 Simulator</span>
    </div>
  );
};

export default TopBar;