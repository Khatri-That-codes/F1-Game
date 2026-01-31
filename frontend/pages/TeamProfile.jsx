import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom"; 
import { fetchTeamDetails } from "../api";
import { useTheme } from "../context/ThemeContext"; 

const TeamProfile = () => {
  const { theme } = useTheme();
  const { teamName } = useParams(); // Get team name from URL
  const [team, setTeam] = useState(null); 
  const [error, setError] = useState(null); 
  const background_Image = "/images/ui/f1_track_background.jpg";

  const teamColour = team ? team.team_colour : "#FFFFFF";
  
  // Fetch team details from the backend
  useEffect(() => {
    fetchTeamDetails(teamName)
      .then((data) => setTeam(data))
      .catch((error) => setError(error.message));
  }, [teamName]);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!team) {
    return <div>Loading...</div>;
  }

  return (
    <div style={{
        backgroundImage: `url(${background_Image})`,
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
      // padding: '40px 20px',
      // fontFamily: '"Press Start 2P", Arial, sans-serif',
      // display: 'flex',
      // flexDirection: 'column',
      // alignItems: 'center'
    }}>
      <h1 style={{ color: "#fff", marginBottom: '40px', textAlign: 'center', fontFamily: '"Press Start 2P", Arial, sans-serif' }}>Team Profile</h1>

      {/* Large White Card */}
      <div style={{
        backgroundColor: teamColour,
        borderRadius: "20px",
        boxShadow: "0 10px 20px rgba(0, 0, 0, 0.2)",
        padding: "40px 20px",
        maxWidth: "1200px",
        width: "100%",
        textAlign: "center",
        alignContent: "center"
      }}>
        {/* Team Logo and Details */}
        <div style={{
          ...styles.header,
          backgroundColor: "#fff",
          boxShadow: `0 8px 16px ${theme.cardShadow}`,
          alignContent: "center",
          margin: "0 auto"
        }}>
          <img src={team.logo_path} alt={team.name} style={styles.logo} />
          <div style= {{textAlign: "left"}}>
            <h1 style={styles.name}>{team.name}</h1>
            <p style={styles.detail}>
              <strong>Base:</strong> {team.base}
            </p>
            <p style={styles.detail}>
              <strong>Principal:</strong> {team.principal}
            </p>
            <p style={styles.detail}>
              <strong>Championships:</strong> {team.championships}
            </p>
          </div>
        </div>

        {/* Drivers Section */}
        <div style={styles.driversSection}>
          <h2 style={styles.sectionTitle}>Drivers</h2>
          <div style={{
            display: "flex", 
            flexDirection: "row", 
            gap: "20px", 
            justifyContent: "center", 
            alignItems: "center" 
          }}>
            {team.drivers.map((driver) => (
              <div key={driver.name} style={styles.driverCard}>
                <img
                  src={driver.driver_image}
                  alt={driver.name}
                  style={styles.driverImage}
                />
                <h3 style={styles.driverName}>{driver.name}</h3>
                <p style={styles.driverDetail}>
                  <strong>Number:</strong> {driver.number}
                </p>
                <p style={styles.driverDetail}>
                  <strong>Nation:</strong> {driver.nation}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

// Inline styles for the page
const styles = {
  container: {
    padding: "40px 20px",
    fontFamily: "'Press Start 2P', Arial, sans-serif",
    minHeight: "100vh",
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center'
  },
  header: {
    display: "flex",
    alignItems: "center",
    marginBottom: "40px",
    borderRadius: "15px",
    padding: "30px",
    maxWidth: "800px",
    width: "100%"
  },
  logo: {
    maxWidth: "300px",
    maxHeight: "200px",
    
    marginRight: "20px",
  },
  details: {
    flex: 1,
  },
  name: {
    fontSize: "2.5rem",
    color: "#000",
    marginBottom: "10px",
    fontFamily: "'Press Start 2P', Arial, sans-serif"
  },
  detail: {
    fontSize: "1rem",
    color: "#000",
    marginBottom: "10px",
    
  },
  driversSection: {
    marginTop: "20px",
  },
  sectionTitle: {
    fontSize: "2rem",
    color: "#fff",
    marginBottom: "20px",
    fontFamily: "'Press Start 2P', Arial, sans-serif"
  },
  driversContainer: {
    display: "flex",
    flexDirection: "row",
    gap: "20px",
    justifyContent: "center",
    alignItems: "center"
  },
  driverCard: {
    backgroundColor: "#fff",
    borderRadius: "10px",
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.5)",
    padding: "20px",
    textAlign: "center",
  },
  driverImage: {
    width: "100px",
    height: "auto",
    borderRadius: "50%",
    marginBottom: "10px",
  },
  driverName: {
    fontSize: "0.8rem",
    color: "#333",
    marginBottom: "10px",
    fontFamily: "'Press Start 2P', Arial, sans-serif"
  },
  driverDetail: {
    fontSize: "1rem",
    color: "#666",
    marginBottom: "5px",
  },

  teamCard:{
    backgroundColor: "#fff",
    borderRadius: "15px",
    padding: "20px",
    boxShadow: `0 4px 8px rgba(0, 0, 0, 0.1)`,
    textAlign: "start",
  }
};

export default TeamProfile;