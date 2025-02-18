import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [token, setToken] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/api/login/', {
                username,
                password,
            });
            setToken(response.data.token);
            alert('ログイン成功');
        } catch (error) {
            alert('ログイン失敗');
        }
    };

    return (
        <div>
            <h2>ユーザ登録</h2>
            <form onSubmit={handleLogin}>
                <label>
                    ユーザ名:
                    <input type='text' name='username' value={username} onChange={(e) => setUsername(e.target.value)} />
                </label>
                <br />
                <label>
                    パスワード:
                    <input type='password' name='password' value={password} onChange={(e) => setPassword(e.target.value)} />
                </label>
                <br />
                <label>
                    メールアドレス:
                    <input type='email' name='email' value={email} onChange={(e) => setEmail(e.target.value)} />
                </label>
                <br />
                <button type='submit'>ログイン</button>
            </form>
            {token && <p>取得したトークン: {token}</p>}
        </div>
    )
};

export default Login;
