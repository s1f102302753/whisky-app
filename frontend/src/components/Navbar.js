import React from 'react';
import '../styles/Navbar.css';

const Navbar = () => {
    return (
        <nav className='navbar'>
            <div>ウイスキー検定クイズ</div>
            <ul className='navbar-list'>
                <li><a href='/'>ホーム</a></li>
                <li><a href='/login'>ログイン</a></li>
            </ul>
        </nav>
    );
};

export default Navbar;
