import React from 'react';
import "../theme.css";

const Button = ({ children, onClick, style, ...props }) => {
  return (
    <button onClick={onClick} style={style} {...props}>
      {children}
    </button>
  );
};

const Card = ({ children, style, ...props }) => {
  return (
    <div className="card" style={style} {...props}>
      {children}
    </div>
  );
};

const Table = ({ headers, data, style, ...props }) => {
  return (
    <table style={style} {...props}>
      <thead>
        <tr>
          {headers.map((header, index) => (
            <th key={index}>{header}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row, rowIndex) => (
          <tr key={rowIndex}>
            {row.map((cell, cellIndex) => (
              <td key={cellIndex}>{cell}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export { Button, Card, Table };