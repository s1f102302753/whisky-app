import React from 'react';

const Choice = ({ choice, onAnswerSelect, isAnswered }) => {
  return (
    <button 
      onClick={() => onAnswerSelect(choice.id)} 
      disabled={isAnswered} // 回答後は選択を無効化
    >
      {choice.text}
    </button>
  );
};

export default Choice;
