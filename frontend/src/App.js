import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import TopPage from "./components/TopPage.js";
import QuestionDisplay from "./components/QuestionDisplay.js";
import Navbar from "./components/Navbar.js";
import Login from "./components/Login.js";
import HomePage from "./components/HomePage.js";

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/level3" element={<TopPage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/quiz" element={<QuestionDisplay />} />
        </Routes>
      </div>
      
    </Router>
  );
}

export default App;
