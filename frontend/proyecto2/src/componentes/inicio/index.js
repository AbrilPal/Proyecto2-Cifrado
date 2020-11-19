import React, { Component } from 'react';
import './style.css';
import Login from '../login/index';
import Registro from '../registro/index';

class Inicio extends Component {
    render() {
        return (
            <div className="auth-container">
                <Login />
                <Registro />
            </div>
        );
    }
}

export default Inicio;