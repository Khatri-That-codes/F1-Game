import React, { createContext, useContext, useState } from 'react';

const ThemeContext = createContext();

const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState({
    backgroundColor: '#ff1801',
    textColor: '#fff',
    primaryColor: '#000',
    primaryHoverColor: '#333',
    cardBackground: 'rgba(0, 0, 0, 0.3)',
    cardShadow: 'rgba(0, 0, 0, 0.5)',
  });

  const toggleTheme = () => {
    setTheme((prevTheme) => ({
      ...prevTheme,
      backgroundColor: prevTheme.backgroundColor === '#000' ? '#fff' : '#000',
      textColor: prevTheme.textColor === '#fff' ? '#000' : '#fff',
    }));
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

const useTheme = () => useContext(ThemeContext);

export { ThemeProvider, useTheme };