import React, { Component } from 'react';
import './style.css';

class Subir extends Component {
	render() {
		return (
			<div className="contenedor_subir">
				<h1 className="titulo_subir">Subir Archivos</h1>
				<p>Escoga un documento que desee subir</p>
				<input className="input_subir" type="file" />
			</div>
		);
	}
}

export default Subir;