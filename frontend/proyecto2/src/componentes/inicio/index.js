import React from 'react';
import './style.css';
import Login from '../login/index';
import Registro from '../registro/index';

function Inicio(){
    return (
        <div className="auth-container">
            <Login />
            <Registro />
        </div>
    );
};

export default Inicio;