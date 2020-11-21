import React, { Component } from 'react';
import './style.css';
import Login from '../login/index';
import Registro from '../registro/index';
import Menu from '../menu/index';
import Subir from '../subir/index';
import Revisar from '../revisar/index';

class Inicio extends Component {
	render() {
		return (
			<div className="auth-container">
				<Login />
				<Registro />
				<Menu />
				<Subir />
				<Revisar />
			</div>
		);
	}
}

export default Inicio;