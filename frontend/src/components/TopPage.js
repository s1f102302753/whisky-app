import React from 'react';
import { useNavigate } from 'react-router-dom';


const TopPage = () => {
    const navigate = useNavigate();

    const handleStartQuiz = () => {
        navigate('quiz');  // /quiznへ遷移
    }

    return (
        <div>
            <h2>ウイスキー検定クイズ</h2>
            
            <button onClick={handleStartQuiz}>スタート</button>
        </div>
    );
};

export default TopPage;
