import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000/api";

// Fetch all drivers
export const fetchDrivers = async () => {
  try {
    const response = await axios.get(`${API_URL}/drivers`);
    return response.data;
  } catch (error) {
    console.error("Error fetching drivers:", error);
    throw error;
  }
};

// Fetch all teams
export const fetchTeams = async () => {
  try {
    const response = await axios.get(`${API_URL}/teams`);
    return response.data;
  } catch (error) {
    console.error("Error fetching teams:", error);
    throw error;
  }
};

// Fetch all tracks
export const fetchTracks = async () => {
  try {
    const response = await axios.get(`${API_URL}/tracks`);
    return response.data;
  } catch (error) {
    console.error("Error fetching tracks:", error);
    throw error;
  }
};

// Fetch details of a specific team
export const fetchTeamDetails = async (teamName) => {
  try {
    const response = await axios.get(`${API_URL}/teams/${teamName}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching details for team ${teamName}:`, error);
    throw error;
  }
};

// Fetch details of a specific driver
export const fetchDriverDetails = async (driverName) => {
  try {
    const response = await axios.get(`${API_URL}/drivers/${driverName}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching details for driver ${driverName}:`, error);
    throw error;
  }
};

// Fetch standings
export const fetchStandings = async () => {
  try {
    const response = await axios.get(`${API_URL}/standings`);
    return response.data;
  } catch (error) {
    console.error("Error fetching standings:", error);
    throw error;
  }
};