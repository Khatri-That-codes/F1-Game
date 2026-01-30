import React, { useState, useEffect } from "react";
import { fetchStandings } from "../api"; // Import centralized API function
import { Table } from "../components/UIComponents";
import { useTheme } from "../context/ThemeContext";

const StandingsScreen = () => {
  const { theme } = useTheme();
  const [standings, setStandings] = useState([]); // Overall standings fetched from the backend

  // Fetch standings from the backend
  useEffect(() => {
    fetchStandings()
      .then((data) => setStandings(data))
      .catch((error) => console.error("Error fetching standings:", error));
  }, []);

  return (
    <div style={{
      backgroundColor: theme.backgroundColor,
      color: theme.textColor,
      minHeight: "100vh",
      padding: "40px 20px",
      fontFamily: '"Press Start 2P", Arial, sans-serif',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center'
    }}>
      <h1 style={{ 
        color: theme.primaryColor, 
        marginBottom: '40px',
        fontSize: '2.5rem',
        textAlign: 'center'
      }}>Season Standings</h1>

      <div style={{
        backgroundColor: theme.cardBackground,
        border: `3px solid ${theme.primaryColor}`,
        borderRadius: '20px',
        padding: '30px',
        maxWidth: '800px',
        width: '100%',
        boxShadow: `0 10px 20px ${theme.cardShadow}`
      }}>

      <Table
        headers={["Position", "Driver", "Team", "Points"]}
        data={standings.map((driver, index) => [
          index + 1,
          driver.name,
          driver.team,
          driver.points,
        ])}
      />
    </div>
    </div>
  );
};

export default StandingsScreen;