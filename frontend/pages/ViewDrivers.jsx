import React, { useState, useEffect } from "react";
import { fetchDrivers } from "../api";

const ViewDrivers = () => {
  const [drivers, setDrivers] = useState([]); // All drivers fetched from the backend
  const [searchQuery, setSearchQuery] = useState(""); // Search query
  const [filteredDrivers, setFilteredDrivers] = useState([]); // Filtered drivers based on search

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
                <li key={driver.name}>{driver.name}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ViewDrivers;