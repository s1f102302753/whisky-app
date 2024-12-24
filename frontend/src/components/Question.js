import React from 'react';
import Choices from './Choices';

const Question = ({ questionText, choices, onAnswerSelect, isAnswered }) => {
  return (
    <div>
      <p>{questionText}</p>
      <div>
        {choices.map((choice) => (
          <Choices
            key={choice.id} 
            choice={choice} 
            onAnswerSelect={onAnswerSelect} 
            isAnswered={isAnswered}
          />
        ))}
      </div>
    </div>
  );
};

export default Question;
