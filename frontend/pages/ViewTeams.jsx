import React, { useState, useEffect } from "react";
import { fetchTeams } from "../api";
import { Card } from "../components/UIComponents";
import { useTheme } from "../context/ThemeContext"; // Corrected the import path
import { useNavigate } from "react-router-dom";

const ViewTeams = () => {
  const { theme } = useTheme() || { theme: {} }; // Ensure theme is always defined
  const [teams, setTeams] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [filteredTeams, setFilteredTeams] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const getTeams = async () => {
      try {
        const data = await fetchTeams();
        setTeams(data);
        setFilteredTeams(data);
      } catch (error) {
        console.error("Error fetching teams:", error);
      }
    };

    getTeams();
  }, []);

  const handleSearchChange = (event) => {
    const query = event.target.value.toLowerCase();
    setSearchQuery(query);

    const filtered = teams.filter((team) =>
      team.name.toLowerCase().includes(query)
    );
    setFilteredTeams(filtered);
  };

  const handleTeamClick = (teamName) => {
    navigate(`/team-profile/${teamName}`);
  };

  return (
    <div style={{ ...styles.container, backgroundColor: theme.backgroundColor, color: theme.textColor }}>
      <h1 style={{ color: theme.primaryColor }}>View Teams</h1>

      <input
        type="text"
        placeholder="Search Teams"
        value={searchQuery}
        onChange={handleSearchChange}
        style={{
          padding: "10px",
          marginBottom: "20px",
          borderRadius: "5px",
          border: `1px solid ${theme.primaryColor}`,
        }}
      />

      <div style={{ display: "grid", gap: "20px" }}>
        {filteredTeams.map((team) => (
          <Card key={team.id} style={styles.card}>
            <h2>{team.name}</h2>
            <p>Principal: {team.principal}</p>
            <p>Base: {team.base}</p>
            <button
              style={styles.button}
              onClick={() => handleTeamClick(team.name)}
            >
              View Profile
            </button>
          </Card>
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
  image: {
    width: "100%",
    borderRadius: "10px",
  },
  name: {
    fontSize: "1.2rem",
    margin: "10px 0",
  },
  base: {
    fontSize: "1rem",
    color: "#555",
  },
  button: {
    backgroundColor: "#000",//theme.primaryColor || "#000", // Fallback color
    color: "#fff",// theme.textColor || "#fff", // Fallback color
    padding: "10px 20px",
    borderRadius: "5px",
    border: "none",
    cursor: "pointer",
  },
};

export default ViewTeams;