import React, { Component } from 'react';
import './style.css';

class Revisar extends Component {
	render() {
		return (
			<div className="contenedor_revisar">
				<h1 className="titulo_revisar">Revisar Archivos</h1>
				<p>Escoga un documento que desee revisar</p>
				<input className="input_revisar" type="file" />
			</div>
		);
	}
}

export default Revisar;