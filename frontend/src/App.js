import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [quizzes, setQuizzes] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/quiz/api/quizzes/")
      .then((response) => {
        setQuizzes(response.data.quizzes);
      })
      .catch((error) => {
        console.error("Error fetching the quizzes:", error);
      });
  }, []);

  return (
    <div>
      <h1>Whisky Quiz</h1>
      <ul>
        {quizzes.map((quiz) => (
          <li key={quiz.id}>
            <strong>Q:</strong> {quiz.question} <br/>
            <strong>A:</strong> {quiz.answer}
          </li>
        ))}
      </ul>
    </div>
  )
}


export default App;
