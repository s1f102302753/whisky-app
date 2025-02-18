import React from 'react';
import { useNavigate } from 'react-router-dom';


const TopPage = () => {
    const navigate = useNavigate();

    const handleStartQuiz = () => {
        navigate('quiz');  // /quiznへ遷移
    }

    return (
        <div>
            <h2>ウイスキー検定3級</h2>
            <p>ウイスキーが好きで、興味を持ちはじめ、ウイスキーの基礎知識を持つ方を対象とした初級レベル。</p>
            <button onClick={handleStartQuiz}>スタート</button>
        </div>
    );
};

export default TopPage;
