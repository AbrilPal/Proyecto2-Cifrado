import React, { Component } from 'react';
import './style.css';

class Revisar extends Component {
	state = {
		credentials: {
			dochash: '',
			codigo: ''
		}
	}

	inputChanged = event => {
		const cred = this.state.credentials;
		cred[event.target.name] = event.target.value;
		this.setState({credentials: cred});
	}

	onChangeHandler = event => {
		var file = event.target.files[0];
		var reader = new FileReader()

		reader.onload = function (event) {
			var filenotencrypted = event.target.result;
			var CryptoJS = require("crypto-js");
			var filencrypted = CryptoJS.SHA256(filenotencrypted);
			var final = filencrypted + ""
			return final
		}
		reader.readAsBinaryString(file);
		var hash = reader.onload(event)
		this.setState({credentials: {dochash: hash}});
	}

	checkHashDoc = event => {
		console.log(this.state.credentials);
		fetch('http://127.0.0.1:8000/validardoc/', {
			method: 'POST', 
			headers: {'Content-Type': 'application/json'},
			body: JSON.stringify(this.state.credentials)
		})
		.then(data => data.json())
		.then(
			data => {
				var datos = JSON.stringify(data, undefined, '\t')
				window.alert(datos)
			}
		)
		.catch(
			error => {
				console.error(error)
			}
		)
	}

	render() {
		return (
			<div className="contenedor_revisar">
				<h1 className="titulo_revisar">Validar Archivos</h1>
				<p>Escoga un documento que desee validar</p>
				<form onSubmit={this.handleSubmit}>
					<input 
						className="input_revisar" 
						type="file" 
						name="dochash"
						onChange={this.onChangeHandler} />
				</form>
				<p>Escriba el codigo brindado</p>
				<input 
					className="input_revisar"
					name="codigo"
					placeholder="Codigo"
					type="text"
					value={this.state.credentials.codigo}
					onChange={this.inputChanged} />
				<button className="boton_revisar" onClick={this.checkHashDoc}>Validar</button>
			</div>
		);
	}
}

export default Revisar;