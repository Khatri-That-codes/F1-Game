import React from "react";
import { useTheme } from "../context/ThemeContext";
import "../theme.css";
import { useNavigate } from "react-router-dom";

const TopBar = ({ title }) => {
  const { theme } = useTheme();
  const navigate = useNavigate();

  const handleBackClick = () => {
    navigate(-1); // Navigates to the previous page
  };

  const styles = {
    container: {
      display: "flex",
      alignItems: "center",
      justifyContent: "flex-start", 
      padding: "10px 20px",
      backgroundColor: "rgba(135, 9, 9, 0.8)", // theme.cardBackground,
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
      fontFamily: "'Press Start 2P',Arial, sans-serif", 
      color: "rgba(255, 255, 255, 0.9)",
       
    },
    backBtn: {
      backgroundColor: "#fff",
      color: "#333",
      border: "none",
      borderRadius: "5px",
      padding: "5px 10px", 
      cursor: "pointer",
      fontFamily: "'Press Start 2P', Arial, sans-serif",
      fontSize: "0.8rem",
      marginLeft: "750px"
    },
  };

  return (
    <div style={styles.container}>
      <img src="/images/ui/f1_logo.png" alt="F1 Logo" style={styles.logo} />
      <span style={styles.title}>F1 Simulator</span>
      <button
        onClick={handleBackClick}
        style={styles.backBtn}
      >
        Back
      </button>
    </div>
  );
};

export default TopBar;