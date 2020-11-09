import React from 'react';
import './style.css';

function Login(){
    return (
        <div className="contenedor_login">
            <h1 class="titulo_login">Login de usuarios</h1>
            <input className="input_login" type="text" placeholder="Username"/>
            <input className="input_login" type="password" placeholder="Password"/>
            <input className="boton_inicio" type="submit" placeholder="Login"/>
        </div>
    );
};

export default Login;