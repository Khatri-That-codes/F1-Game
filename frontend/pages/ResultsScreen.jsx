import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { Button, Card } from "../components/UIComponents";
import { useTheme } from "../context/ThemeContext";

const ResultsScreen = () => {
  const { theme } = useTheme();
  const location = useLocation();
  const navigate = useNavigate();
  const raceResults = location.state?.raceResults;

  if (!raceResults) {
    return (
      <div style={{
        backgroundColor: theme.backgroundColor,
        color: theme.textColor,
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
      }}>
        <h1 style={{ color: theme.primaryColor }}>No Results Available</h1>
        <Button onClick={() => navigate("/")}>Go Back</Button>
      </div>
    );
  }

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
      }}>Race Results</h1>

      <div style={{ 
        display: "grid", 
        gap: "20px",
        width: '100%',
        maxWidth: '800px'
      }}>
        {raceResults.final_results.map((driver, index) => (
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
              color: index < 3 ? theme.textColor : theme.textColor,
            }}
          >
            <h2>Position: {index + 1}</h2>
            <h3>Driver: {driver}</h3>
            <p>Points: {25 - index * 7}</p>
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