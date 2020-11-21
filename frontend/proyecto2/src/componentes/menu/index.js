import React, { Component } from 'react';
import './style.css';

class Menu extends Component {
	render() {
		return (
			<div className="contenedor_menu">
				<h1 className="titulo_menu">Menu Principal</h1>
				<button className="boton_menu" onClick={this.register}>Subir Archivo</button>
				<button className="boton_menu" onClick={this.register}>Revisar Archivo</button>
			</div>
		);
	}
}

export default Menu;