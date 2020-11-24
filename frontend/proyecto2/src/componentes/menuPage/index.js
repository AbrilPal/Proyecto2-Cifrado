import React, { Component } from 'react';
import './style.css';
import Login from '../login/index';
import Registro from '../registro/index';
import Menu from '../menu/index';

class MenuPage extends Component {
	render() {
		return (
			<div className="auth-container">
				<Menu />
			</div>
		);
	}
}

export default MenuPage;