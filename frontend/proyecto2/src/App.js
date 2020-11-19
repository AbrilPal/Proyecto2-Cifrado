import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          QUE ONDA PERROS! ♥ http://127.0.0.1:8000/
        </p>
      </header> */}
      <section className="loginDiv">
        <div className="loginForm">
          <h1 class="title">Login de usuarios</h1>
          <br />
          <input className="controls" type="text" placeholder="Username"/>
          <br />
          <input className="controls" type="password" placeholder="Password"/>
          <br />
          <input className="button" type="submit" placeholder="Login"/>
        </div>
      </section>
    </div>
  );
}

export default App;
