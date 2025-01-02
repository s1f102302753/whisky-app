import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import TopPage from "./components/TopPage.js";
import QuestionDisplay from "./components/QuestionDisplay.js";
import Navbar from "./components/Navbar.js";
import UserRegister from "./components/UserRgister.js";

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<TopPage />} />
          <Route path="/login" element={<UserRegister />} />
          <Route path="/quiz" element={<QuestionDisplay />} />
        </Routes>
      </div>
      
    </Router>
  );
}

export default App;
