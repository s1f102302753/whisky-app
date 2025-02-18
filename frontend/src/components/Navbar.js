import React from 'react';
import '../styles/Navbar.css';

const Navbar = () => {
    return (
        <nav className='navbar'>
            <div>ウイスキー検定クイズ</div>
            <ul className='navbar-list'>
                <li><a href='/'>Home</a></li>
                <li><a href='level1'>1級</a></li>
                <li><a href='level2'>2級</a></li>
                <li><a href='level3'>3級</a></li>
                <li><a href='/login'>ログイン</a></li>
            </ul>
        </nav>
    );
};

export default Navbar;
