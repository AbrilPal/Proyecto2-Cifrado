import React, { Component } from 'react';
import './style.css';

class Subir extends Component {
	state = {
		credentials: {
			dochash: ''
		}
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
	
	registerHashDoc = event => {
		console.log(this.state.credentials);
		fetch('http://127.0.0.1:8000/registrardoc/', {
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
			<div className="contenedor_subir">
				<h1 className="titulo_subir">Subir Archivos</h1>
				<p>Escoga un documento que desee subir</p>
				<input 
					className="input_subir" 
					type="file" 
					name="dochash"
					onChange={this.onChangeHandler}/>
				<button className="boton_subir" onClick={this.registerHashDoc}>Subir</button>
				<h3>Tomar nota del codigo</h3>
			</div>
		);
	}	
}

export default Subir;