import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom"; 
import { fetchDriverDetails } from "../api";
import { useTheme } from "../context/ThemeContext"; 

const DriverProfile = () => {
  const { theme } = useTheme();
  const { driverName } = useParams(); // Getting name of driver from url
  const [driver, setDriver] = useState(null); 
  const [error, setError] = useState(null); 

  // Fetch driver details from the backend
  useEffect(() => {
    fetchDriverDetails(driverName)
      .then((data) => setDriver(data))
      .catch((error) => setError(error.message));
  }, [driverName]);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!driver) {
    return <div>Loading...</div>;
  }

  return (
    <div style={{
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

      // backgroundColor: theme.backgroundColor,
      // color: theme.textColor,
      // minHeight: '100vh',
      // padding: '20px 20px',
      // fontFamily: '"Press Start 2P", Arial, sans-serif',
      // display: 'flex',
      // flexDirection: 'column',
      // alignItems: 'center',
      // justifyContent: 'center'
    }}>
      <h1 style={{ color: theme.primaryColor, marginBottom: '40px', textAlign: 'center' , fontFamily: "'Press Start 2P', Arial, sans-serif"}}>Driver Profile</h1>
      <div style={{
        ...styles.container,
        backgroundColor: theme.cardBackground,
        boxShadow: `0 8px 16px ${theme.cardShadow}`
      }}>
      {/* Driver Image */}
      <div style={styles.imageContainer}>
        <img
          src={driver.driver_image}
          alt={driver.name}
          style={styles.image}
        />
      </div>

      {/* Driver Details */}
      <div style={styles.detailsContainer}>
        <h1 style={styles.name}>{driver.name}</h1>
        <h2 style={styles.team}>Team: {driver.team_name}</h2>
        <p style={styles.detail}>
          <strong>Number:</strong> {driver.number}
        </p>
        <p style={styles.detail}>
          <strong>Nation:</strong> {driver.nation}
        </p>
        <p style={styles.detail}>
          <strong>XP:</strong> {driver.xp}
        </p>
        <p style={styles.detail}>
          <strong>Aggression:</strong> {driver.aggression}
        </p>
        <p style={styles.detail}>
          <strong>Qualifying Skill:</strong> {driver.qualifying}
        </p>
      </div>
    </div>
    </div>
  );
};

// Inline styles for the page
const styles = {
  container: {
    display: "flex",
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    padding: "30px",
    fontFamily: "'Press Start 2P', Arial, sans-serif",
    borderRadius: "15px",
    maxWidth: "900px",
    width: "100%",
  },
  imageContainer: {
    flex: 1,
    textAlign: "center",
  },
  image: {
    width: "300px",
    height: "auto",
    borderRadius: "10px",
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.2)",
  },
  detailsContainer: {
    flex: 2,
    padding: "20px",
  },
  name: {
    fontSize: "1rem",
    color: "#fff",
    marginBottom: "10px",
    fontFamily: "'Press Start 2P', Arial, sans-serif"
  },
  team: {
    fontSize: "1rem",
    color: "#ffffff",
    marginBottom: "20px",
    fontFamily: "'Press Start 2P', Arial, sans-serif"
  },
  detail: {
    fontSize: "1rem",
    color: "#fff",
    marginBottom: "10px",
  },
};

export default DriverProfile;