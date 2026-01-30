import React, { useState, useEffect } from "react";
import { fetchTeams } from "../api";
import { Card } from "../components/UIComponents";
import { useTheme } from "../context/ThemeContext";

const ViewTeams = () => {
  const { theme } = useTheme();
  const [teams, setTeams] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [filteredTeams, setFilteredTeams] = useState([]);

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

  return (
    <div style={{
      backgroundColor: theme.backgroundColor,
      color: theme.textColor,
      minHeight: "100vh",
      padding: "20px",
    }}>
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
          <Card key={team.id}>
            <h2>{team.name}</h2>
            <p>Principal: {team.principal}</p>
            <p>Base: {team.base}</p>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default ViewTeams;