import React from 'react';
import './login.css';

function Login() {
  return (
    <div className="App">
      <section className="loginDiv">
        <div className="loginForm">
          <h1 class="title">Login de Usuarios</h1>
          <br />
          <input className="controls" type="text" placeholder="Username" />
          <br />
          <input className="controls" type="password" placeholder="Password" />
          <br />
          <button className="button">Login</button>
        </div>
      </section>
    </div>
  );
}

export default Login;