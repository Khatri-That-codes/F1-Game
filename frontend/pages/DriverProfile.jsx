import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom"; 
import { fetchDriverDetails } from "../api"; 

const DriverProfile = () => {
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
    <div style={styles.container}>
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
  );
};

// Inline styles for the page
const styles = {
  container: {
    display: "flex",
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    padding: "20px",
    fontFamily: "'Arial', sans-serif",
    backgroundColor: "#f4f4f9",
    borderRadius: "10px",
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
    maxWidth: "800px",
    margin: "40px auto",
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
    fontSize: "2rem",
    color: "#333",
    marginBottom: "10px",
  },
  team: {
    fontSize: "1.5rem",
    color: "#555",
    marginBottom: "20px",
  },
  detail: {
    fontSize: "1rem",
    color: "#666",
    marginBottom: "10px",
  },
};

export default DriverProfile;