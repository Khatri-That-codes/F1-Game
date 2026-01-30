import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import MainMenu from "./pages/MainMenu";
import RaceScreen from "./pages/RaceScreen";
import RaceIntroScreen from "./pages/RaceIntroScreen";
import ResultsScreen from "./pages/ResultsScreen";
import ViewDrivers from "./pages/ViewDrivers";
import ViewTeams from "./pages/ViewTeams";
import StandingsScreen from "./pages/StandingsScreen";
import TopBar from "./components/TopBar";
import TrackSelectScreen from "./pages/TrackSelectScreen";
import DriverProfile from "./pages/DriverProfile";
import TeamProfile from "./pages/TeamProfile";

const App = () => {
  return (
    <Router>
      <TopBar />
      <Routes>
        {/* Main Menu */}
        <Route path="/" element={<MainMenu />} />

        {/* Race Flow */}
        <Route path="/track-select" element={<TrackSelectScreen />} />
        <Route path="/race-intro" element={<RaceIntroScreen />} />
        <Route path="/race-screen" element={<RaceScreen />} />
        <Route path="/race" element={<RaceScreen />} />
        <Route path="/results" element={<ResultsScreen />} />

        {/* Other Pages */}
        <Route path="/drivers" element={<ViewDrivers />} />
        <Route path="/teams" element={<ViewTeams />} />
        <Route path="/standings" element={<StandingsScreen />} />

        <Route path="/view-drivers" element={<ViewDrivers />} />
        <Route path="/driver-profile/:driverName" element={<DriverProfile />} />
        <Route path="/view-teams" element={<ViewTeams />} />
        <Route path="/team-profile/:teamName" element={<TeamProfile />} />
      </Routes>
    </Router>
  );
};

export default App;