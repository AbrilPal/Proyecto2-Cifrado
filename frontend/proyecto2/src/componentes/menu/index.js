import React, { Component } from 'react';
import { Link } from "react-router-dom";
import './style.css';

class Menu extends Component {
	render() {
		return (
			<div className="contenedor_menu">
				<h1 className="titulo_menu">Menu Principal</h1>
				<Link to="/subir">
					<button className="boton_menu" onClick={this.register}>Subir Archivo</button>
          		</Link>
				<Link to="/revisar">
				<button className="boton_menu" onClick={this.register}>Revisar Archivo</button>
				</Link>
			</div>
		);
	}
}

export default Menu;