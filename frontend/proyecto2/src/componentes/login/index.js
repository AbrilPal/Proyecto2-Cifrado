import React, { Component } from 'react';
import './style.css';
// import { MDBBtn } from 'mdbreact';
import axios from 'axios';

class Login extends Component {

    constructor(props) {
        super(props);

        this.state={
            usuario: null,
            clave: null
        };

        this.handleChange = this.handleChange.bind(this);
        this.submit = this.submit.bind(this);
    }

    handleChange(e) {
        let name = e.target.name;
        let value = e.target.value;
        // console.log(name, value);
        let data={};
        data[name]=value;

        this.setState(data);
        console.log(data)
    };

    render() {
        return (
            <form className="contenedor_login" onSubmit={this.submit} >
                <h1 className="titulo_login">Login de usuarios</h1>
                <input className="input_login" name="usuario" type="text" value={this.state.usuario || ''} placeholder="Usuario" onChange={this.handleChange} />
                <input className="input_login" name="clave" type="password" value={this.state.clave || ''} placeholder="Contraseña" onChange={this.handleChange} />
                <input className="boton_inicio" type="submit" value="Iniciar Sesion" />
                {/* <MDBBtn
                    // outline
                    color="white"
                    className="boton_inicio"
                >Inicio Sesion</MDBBtn> */}
            </form>
        );

    };
    submit(e) {
        e.preventDefault();
        axios.post('/login/', {
            usuario: this.state.usuario, 
            clave: this.state.clave
        }
        )
        .then(response => {
            console.log(response);
        }).catch(response => {
            console.log(response)
        })
        ;
    };
}
export default Login;