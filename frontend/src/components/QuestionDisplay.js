import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Question from './Question';
import AnswerFeedback from './AnswerFeedback';

const QuestionDisplay = () => {
  const [question, setQuestion] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [showExplanation, setShowExplanation] = useState(false);

  useEffect(() => {
    axios.get('http://localhost:8000/api/question/1/')
      .then(response => {
        setQuestion(response.data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, []);

  const handleAnswerSelect = (choiceId) => {
    setSelectedAnswer(choiceId);
    setIsAnswered(true);
    setShowExplanation(true);

    axios.post('http://localhost:8000/api/user-scores/', {
      question_id: question.id,
      choice_id: choiceId,
    })
    .then(response => {
      console.log('回答結果:', response.data);
    })
    .catch(error => {
      console.error('回答送信中にエラーが発生しました:', error);
    });
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  if (!question) return <div>No question available.</div>;

  return (
    <div>
      <h2>問題</h2>
      <Question 
        questionText={question.text}
        choices={question.choices}
        onAnswerSelect={handleAnswerSelect}
        isAnswered={isAnswered}
      />
      {showExplanation && (
        <AnswerFeedback explanation={question.explanation} />
      )}
    </div>
  );
};

export default QuestionDisplay;
