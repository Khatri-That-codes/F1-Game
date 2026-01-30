import React, { useState, useEffect } from "react";
import { fetchDrivers } from "../api";
import { useNavigate } from "react-router-dom";

const ViewDrivers = () => {
  const [drivers, setDrivers] = useState([]); // All drivers fetched from the backend
  const [searchQuery, setSearchQuery] = useState(""); // Search query
  const [filteredDrivers, setFilteredDrivers] = useState([]); 
  const navigate = useNavigate();

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
    navigate(`/driver-profile/${driverName}`);
  };

  return (
    <div>
      <h1>View Drivers</h1>

      {/* Search Bar */}
      <div>
        <input
          type="text"
          placeholder="Search for a driver..."
          value={searchQuery}
          onChange={handleSearchChange}
        />
      </div>

      {/* Display Drivers by Team */}
      <div>
        {Object.keys(driversByTeam).map((team) => (
          <div key={team}>
            <h2>{team}</h2>
            <ul>
              {driversByTeam[team].map((driver) => (
                <li key={driver.name}>
                  <div
                    style={styles.card}
                    onClick={() => handleDriverClick(driver.name)}
                  >
                    <img
                      src={driver.driver_image}
                      alt={driver.name}
                      style={styles.image}
                    />
                    <h3 style={styles.name}>{driver.name}</h3>
                    <p style={styles.team}>{driver.team_name}</p>
                  </div>
                </li>
              ))}
            </ul>
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
    gap: "20px",
    padding: "20px",
  },
  card: {
    cursor: "pointer",
    width: "200px",
    textAlign: "center",
    padding: "10px",
    borderRadius: "10px",
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
    transition: "transform 0.2s",
  },
  cardHover: {
    transform: "scale(1.05)",
  },
  image: {
    width: "100%",
    borderRadius: "10px",
  },
  name: {
    fontSize: "1.2rem",
    margin: "10px 0",
  },
  team: {
    fontSize: "1rem",
    color: "#555",
  },
};

export default ViewDrivers;