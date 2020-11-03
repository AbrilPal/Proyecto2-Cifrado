import React from 'react';
import './register.css';

function Register() {
  return (
    <div className="App">
      <section className="loginDiv">
        <div className="loginForm">
            <h1 class="title">Registro de usuarios</h1>
          <br />
          <input className="controls" type="text" placeholder="Username" />
          <br />
          <input className="controls" type="text" placeholder="Email" />
          <br />
          <input className="controls" type="password" placeholder="Password" />
          <br />
          <button className="button">Registro</button>
        </div>
      </section>
    </div>
  );
}

export default Register;