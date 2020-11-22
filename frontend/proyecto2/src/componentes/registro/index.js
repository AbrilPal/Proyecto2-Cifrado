import React, { Component } from 'react';
import './style.css';

class Registro extends Component {
	state = {
		credentials: {
			nombres: '',
			apellidos: '',
			usuario: '',
			clave: ''
		}
	}

	register = event => {
		console.log(this.state.credentials);
		fetch('http://127.0.0.1:8000/registro/', {
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
			<div className="contenedor_registro">
				<h1 className="titulo_registro">Registro de usuarios</h1>
				<input 
					className="input_registro" 
					name="nombres" 
					type="text" 
					placeholder="Nombres" 
					value={this.state.credentials.nombres} 
					onChange={this.inputChanged} />
				<input 
					className="input_registro" 
					name="apellidos" 
					type="text" 
					placeholder="Apellidos" 
					value={this.state.credentials.apellidos} 
					onChange={this.inputChanged} />
				<input 
					className="input_registro" 
					name="usuario" 
					type="text" 
					placeholder="Usuario" 
					value={this.state.credentials.usuario} 
					onChange={this.inputChanged} />
				<input 
					className="input_registro" 
					name="clave" 
					type="password" 
					placeholder="Contraseña" 
					value={this.state.credentials.clave}
					onChange={this.inputChanged} />
				<button className="boton_registro" onClick={this.register}>Registrarse</button>
			</div>
		);
	}
}

export default Registro;