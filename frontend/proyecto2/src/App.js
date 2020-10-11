import React from 'react';
import logo from './logo.svg';
import './App.css';


function callApiGET(){
  fetch("http://127.0.0.1:8000/testget/", {
    "method": "GET",
    "Access-Control-Allow-Origin": "http://127.0.0.1:8000/"
  })
  .then(response => response.json())
  .then(response => {
    console.log('llamada al api ------------>',response.response)
  })
  .catch(err => { console.log(err); 
  });

 
}


function App() {
  // llamada al servicio
  callApiGET()
  //fin
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          QUE ONDA PERROS! ♥
        </p>
      </header>
    </div>
  );
}

export default App;
