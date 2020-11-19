import React, { Component } from 'react';
import './style.css';
// import { MDBBtn } from 'mdbreact';

class Registro extends Component {
    render() {
        return (
            <form className="contenedor_registro">
                <h1 className="titulo_registro">Registro de usuarios</h1>
                <input className="input_login" type="text" placeholder="Nombre"/>
                <input className="input_login" type="text" placeholder="Apellido"/>
                <input className="input_login" type="text" placeholder="Usuario"/>
                <input className="input_login" type="password" placeholder="Contraseña"/>
                <input className="boton_registro" type="submit" value="Registrarse"/>
                {/* <MDBBtn
                    outline
                    color="black"
                    className="boton_registro"
                >Registrarse</MDBBtn> */}
            </form>
        );
    }
}

export default Registro;