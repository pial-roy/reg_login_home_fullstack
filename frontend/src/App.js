// frontend/src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import RegisterPage from './pages/RegisterPage';
import LoginPage from './pages/LoginPage';
import HomePage from './pages/HomePage';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/" element={
          <div>
            <h1>Welcome to the Retail Auction App!</h1>
            <p>Go to <a href="/register">Register</a> or <a href="/login">Login</a></p>
          </div>
        } />
      </Routes>
    </Router>
  );
};

export default App;