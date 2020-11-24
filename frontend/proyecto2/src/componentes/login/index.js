import React, { Component } from 'react';
import './style.css';
import { Link } from "react-router-dom";

class Login extends Component {

	state = {
		credentials: {
			usuario: '',
			clave: ''
		}
	}

	login = event => {
		console.log(this.state.credentials);
		fetch('http://127.0.0.1:8000/login/', {
			method: 'POST', 
			headers: {'Content-Type': 'application/json'},
			body: JSON.stringify(this.state.credentials)
		})
		.then(data => data.json())
		.then(
			data => {
					console.log(data)
			}
		)
		.catch(error => console.error(error))
	}

	inputChanged = event => {
		const cred = this.state.credentials;
		cred[event.target.name] = event.target.value;
		this.setState({credentials: cred});
	}

	render() {
		return (
			<div className="contenedor_login">
				<h1 className="titulo_login">Login de usuarios</h1>
				<input 
					className="input_login" 
					name="usuario" 
					type="text" 
					placeholder="Usuario" 
					value={this.state.credentials.usuario} 
					onChange={this.inputChanged} />
				<input 
					className="input_login" 
					name="clave" 
					type="password" 
					placeholder="Contraseña" 
					value={this.state.credentials.clave}
					onChange={this.inputChanged} />
				<Link to="/menu">
					<button className="boton_inicio" onClick={this.login}>Iniciar Sesion</button>
          		</Link>
			</div>

		);
	};
}
export default Login;