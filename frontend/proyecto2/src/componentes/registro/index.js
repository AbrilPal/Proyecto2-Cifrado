import React from 'react';
import './style.css';
import { MDBBtn } from 'mdbreact';

function Registro(){
    return (
        <div className="contenedor_registro">
            <h1 class="titulo_registro">Registro de usuarios</h1>
            <input className="input_login" type="text" placeholder="Usuario"/>
            <input className="input_login" type="password" placeholder="Contraseña"/>
            <MDBBtn
                outline
                color="black"
                className="boton_registro"
            >Registrarse</MDBBtn>
        </div>
    );
};

export default Registro;