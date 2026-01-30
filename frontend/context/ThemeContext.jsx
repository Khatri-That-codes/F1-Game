import React, { createContext, useContext, useState } from 'react';

const ThemeContext = createContext();

const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState({
    backgroundColor: '#000',
    textColor: '#fff',
    primaryColor: '#ff1801',
    primaryHoverColor: '#d41601',
    cardBackground: '#111',
    cardShadow: 'rgba(0, 0, 0, 0.2)',
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