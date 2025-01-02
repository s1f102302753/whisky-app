import React, { useState } from 'react';
import axios from 'axios';

const UserRegister = () => {
    const [formData, setFormatData] = useState({
        username: '',
        password: '',
        email: '',
    });
    const [message, setMessage] = useState('');

    const handleChange = (e) => {
        const { name, value} = e.target;
        setFormatData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/api/user/', formData);
            setMessage(response.data.message);
        } catch (error) {
            setMessage('Register failed');
        }
    };

    return (
        <div>
            <h2>ユーザ登録</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    ユーザ名:
                    <input type='text' name='username' value={formData.username} onChange={handleChange} required />
                </label>
                <br />
                <label>
                    パスワード:
                    <input type='password' name='password' value={formData.password} onChange={handleChange} required />
                </label>
                <br />
                <label>
                    メールアドレス:
                    <input type='email' name='email' value={formData.email} onChange={handleChange} required />
                </label>
                <br />
                <button type='submit'>登録</button>
            </form>
            {message && <div>{message}</div>}
        </div>
    )
};

export default UserRegister;
