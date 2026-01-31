import React, { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { Button, Card } from "../components/UIComponents";
import { useTheme } from "../context/ThemeContext";
import { fetchDrivers } from "../api";

const ResultsScreen = () => {
  const { theme } = useTheme();
  const navigate = useNavigate();
  const [raceResults, setRaceResults] = useState([]);
  const [playerXP, setPlayerXP] = useState(0);

  useEffect(() => {
    const fetchAndSetDrivers = async () => {
      try {
        const drivers = await fetchDrivers();

        // Shuffle drivers to assign random positions
        const shuffledDrivers = drivers.sort(() => Math.random() - 0.5);
        setRaceResults(shuffledDrivers);

        // Calculate and update player XP based on points
        const totalXP = shuffledDrivers.reduce((xp, _, index) => xp + Math.max(25 - index * 7, 0), 0);
        setPlayerXP(totalXP);
      } catch (error) {
        console.error("Error fetching drivers:", error);
      }
    };

    fetchAndSetDrivers();
  }, []);

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
        Race Results
      </h1>

      <div
        style={{
          display: "grid",
          gap: "20px",
          width: "100%",
          maxWidth: "800px",
        }}
      >
        {raceResults.map((driver, index) => (
          <Card
            key={driver}
            style={{
              backgroundColor:
                index === 0
                  ? theme.primaryColor
                  : index === 1
                  ? "#d4af37"
                  : index === 2
                  ? "#c0c0c0"
                  : theme.cardBackground,
              color: theme.textColor,
            }}
          >
            <h2>Position: {index + 1}</h2>
            <h3>Driver: {driver.name}</h3>
            <p>Points: {Math.max(25 - index * 7, 0)}</p>
          </Card>
        ))}
      </div>

      <div style={{ marginTop: "20px" }}>
        <Button onClick={() => navigate("/")}>Go Back</Button>
      </div>
    </div>
  );
};

export default ResultsScreen;