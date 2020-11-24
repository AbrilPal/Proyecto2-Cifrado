import React from 'react';
import { BrowserRouter, Route, Switch, Redirect} from "react-router-dom";
import Inicio from './componentes/inicio/index';
import MenuPage from './componentes/menuPage/index';
import SubirPage from './componentes/subirPage/index';
import RevisarPage from './componentes/revisarPage/index';
import './App.css';

function App() {
  return (
    <BrowserRouter>
    <Switch>
      <Route exact path="/inicio" component={Inicio} />
      <Route exact path="/menu" component={MenuPage}/>
      <Route exact path="/subir" component={SubirPage} />
      <Route exact path="/revisar" component={RevisarPage} />
      <Route render={() => <Redirect to="/inicio" />} />
    </Switch>
    </BrowserRouter>
  );
}

export default App;
