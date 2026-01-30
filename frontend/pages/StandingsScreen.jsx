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
      padding: "20px",
    }}>
      <h1 style={{ color: theme.primaryColor }}>Season Standings</h1>

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
  );
};

export default StandingsScreen;