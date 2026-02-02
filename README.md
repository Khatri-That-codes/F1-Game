# F1 Game Simulator

This project is an attempt towards full stack dev with the use of:
### Frontend
- **React**: For building the user interface.
- **React Router**: For managing navigation between pages.
- **CSS**: Custom global styles for a consistent F1 theme.

### Backend
- **FastAPI**: For creating RESTful API endpoints.
- **Python**: Core logic for race simulation and data management.


Currently deployed on **Render**

## Project Outline
An interactive F1 racing simulation game where users can:
- Select a track and simulate a race.
- View detailed driver profiles.
- Explore team profiles and their drivers.
- Check the overall standings for the season.

## Features

### 1. Main Menu
- A starting point for the application with options to:
  - Start a race.
  - View drivers.
  - View teams.
  - View standings.

### 2. Race Simulation
- Select a track and view its details.
- Simulate qualifying and final races.
- Display race results with commentary.

### 3. Driver Profiles
- View detailed information about each driver, including:
  - Name, team, number, and nationality.
  - Driver image and stats.

### 4. Team Profiles
- Explore team details, including:
  - Team name, base, principal, and championships.
  - Drivers associated with the team.

### 5. Standings
- View the overall standings for the season.
- Highlight the top 3 positions with gold, silver, and bronze themes.



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/f1-game.git
   ```

2. Navigate to the project directory:
   ```bash
   cd f1-game
   ```

3. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

5. Start the backend server:
   ```bash
   uvicorn backend.main:app --reload
   ```

4. Open another terminal, Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

6. Start the frontend development server:
   ```bash
   npm run dev
   ```

## Folder Structure

```
F1-Game/
├── backend/
│   ├── api/                # API endpoints
│   ├── data/               # Data models and placeholder data
│   ├── src/                # Core logic for race simulation
├── frontend/
│   ├── pages/              # React components for each page
│   ├── main.jsx            # Entry point for the React app
│   ├── index.css           # Global styles
├── README.md               # Project documentation
```

#### Made with love by Jena <3