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
  const background_Image = "/assets/images/ui/empty_grandstand.webp";

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
    const formattedName = teamName.replace(" ", "_").toLowerCase();
    navigate(`/team-profile/${encodeURIComponent(formattedName)}`);
  };

  return (
    <div style={{
        backgroundImage: `url(${background_Image})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        minHeight: "100vh",
        padding: "70px 20px",
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
      {/* <h1 style={{ color: theme.primaryColor, marginBottom: '30px', textAlign: 'center', fontSize: '2rem' }}>View Teams</h1> */}

      <input
        type="text"
        placeholder="Search Teams"
        value={searchQuery}
        onChange={handleSearchChange}
        style={{
          padding: "15px 20px",
          marginBottom: "30px",
          borderRadius: "10px",
          border: `2px solid ${theme.primaryColor}`,
          backgroundColor: theme.cardBackground,
          color: theme.textColor,
          fontFamily: '"Press Start 2P", Arial, sans-serif',
          fontSize: '0.8rem',
          width: '100%',
          maxWidth: '400px'
        }}
      />

      <div style={{ 
        display: "grid", 
        gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
        gap: "30px",
        width: '100%',
        maxWidth: '1200px'
      }}>
        {filteredTeams.map((team) => (
          <div key={team.id} style={{
            ...styles.card,
            backgroundColor: theme.cardBackground,
            boxShadow: `0 8px 16px ${theme.cardShadow}`,
            border: `2px solid ${theme.primaryColor}`, 
            alignItems: "center",
          }} onClick={() => handleTeamClick(team.name)}>
            <h2 style={{fontFamily: '"Press Start 2P", Arial, sans-serif', color: "#fff"}}>{team.name}</h2>
            <img
                  src={team.logo_path}
                    alt={team.name}
                    style={styles.image}
            />
            <br></br>
            <h2 style={{fontFamily: 'sans-serif', color: "#fff", fontSize: "1rem"}}>Principal: {team.principal}</h2>
            <h2 style={{fontFamily: ' sans-serif', color: "#fff", fontSize: "1rem"}}>Base: {team.base}</h2>
            {/* <button
              style={styles.button}
              onClick={() => handleTeamClick(team.name)}
            >
              View Profile
            </button> */}
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
    backgroundColor: "#fff",
  },
  image: {
    width: "100%",
    borderRadius: "10px",
    maxHeight: "100px",
    maxWidth: "150px",
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