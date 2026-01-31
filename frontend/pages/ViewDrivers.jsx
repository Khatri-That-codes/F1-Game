import React, { useState, useEffect } from "react";
import { fetchDrivers } from "../api";
import { useNavigate } from "react-router-dom";
import { useTheme } from "../context/ThemeContext";

const ViewDrivers = () => {
  const { theme } = useTheme();
  const [drivers, setDrivers] = useState([]); // All drivers fetched from the backend
  const [searchQuery, setSearchQuery] = useState(""); // Search query
  const [filteredDrivers, setFilteredDrivers] = useState([]); 
  const navigate = useNavigate();
  const background_Image = "/public/images/ui/empty_grandstand.webp";

  // Fetch drivers from the backend
  useEffect(() => {
    const getDrivers = async () => {
      try {
        const data = await fetchDrivers();
        setDrivers(data);
        setFilteredDrivers(data); // Initialize filtered drivers
      } catch (error) {
        console.error("Error fetching drivers:", error);
      }
    };

    getDrivers();
  }, []);

  // Handle search input change
  const handleSearchChange = (event) => {
    const query = event.target.value.toLowerCase();
    setSearchQuery(query);

    // Filter drivers based on the search query
    const filtered = drivers.filter((driver) =>
      driver.name.toLowerCase().includes(query)
    );
    setFilteredDrivers(filtered);
  };

  // Group drivers by team
  const driversByTeam = filteredDrivers.reduce((groups, driver) => {
    const team = driver.team_name;
    if (!groups[team]) {
      groups[team] = [];
    }
    groups[team].push(driver);
    return groups;
  }, {});

  const handleDriverClick = (driverName) => {
    const formattedName = driverName.replace(" ", "_").toLowerCase();
    navigate(`/driver-profile/${encodeURIComponent(formattedName)}`);
  };

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
    }}>
      <h1 style={{ color: theme.primaryColor, marginBottom: '30px', textAlign: 'center', fontSize: '1.8rem', fontFamily: '"Press Start 2P", Arial, sans-serif' }}>Drivers</h1>

      {/* Search Bar */}
      <div style={{ marginBottom: '40px', width: '100%', maxWidth: '350px', alignItems: 'center' }}>
        <input
          type="text"
          placeholder="Search for a driver..."
          value={searchQuery}
          onChange={handleSearchChange}
          style={{
            padding: "15px 20px",
            borderRadius: "10px",
            border: `2px solid ${theme.primaryColor}`,
            backgroundColor: theme.cardBackground,
            color: theme.textColor,
            fontFamily: '"Press Start 2P", Arial, sans-serif',
            fontSize: '0.8rem',
            width: '100%'
          }}
        />
      </div>

      {/* Display Drivers by Team */}
      <div style={{ width: '100%', maxWidth: '1200px' }}>
        {Object.keys(driversByTeam).map((team) => (
          <div key={team} style={{ marginBottom: '50px' }}>
            <h2 style={{ 
              color: theme.primaryColor, 
              textAlign: 'center', 
              marginBottom: '30px',
              fontSize: '1.5rem',
              borderBottom: `2px solid ${theme.primaryColor}`,
              paddingBottom: '10px',
              fontFamily: '"Press Start 2P", Arial, sans-serif'
            }}>{team}</h2>
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
              gap: '25px',
              padding: '0 20px'
            }}>
              {driversByTeam[team].map((driver) => (
                <div key={driver.name} style={{
                  ...styles.card,
                  backgroundColor:  theme.cardBackground,
                  boxShadow: `0 8px 16px ${theme.cardShadow}`,
                  border: `2px solid ${theme.primaryColor}`
                }} onClick={() => handleDriverClick(driver.name)}>
                  <img
                    src={driver.driver_image}
                    alt={driver.name}
                    style={styles.image}
                  />
                  <h3 style={{ ...styles.name, color: theme.textColor }}>{driver.name}</h3>
                  <p style={{ ...styles.team, color: theme.primaryColor }}>{driver.team_name}</p>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    flexWrap: "wrap",
    justifyContent: "center",
    gap: "30px",
    padding: "40px 20px",
  },
  card: {
    cursor: "pointer",
    textAlign: "center",
    padding: "25px",
    borderRadius: "15px",
    transition: "transform 0.3s, box-shadow 0.3s",
    fontFamily: '"Press Start 2P", Arial, sans-serif',
    color: 'rgba(255, 255, 255, 0.9)'
   
  },
  cardHover: {
    transform: "scale(1.05)",
  },
  image: {
    width: "100%",
    maxWidth: "150px",
    height: "150px",
    objectFit: "cover",
    borderRadius: "10px",
    marginBottom: "15px"
  },
  name: {
    fontSize: "1rem",
    margin: "15px 0 10px 0",
  },
  team: {
    fontSize: "0.8rem",
    fontWeight: "bold"
  },
};

export default ViewDrivers;