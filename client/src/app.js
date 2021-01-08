import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom'

import { Login } from './components/login'



function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path='/session'>
          <Login />
        </Route>
      </Switch>
    </BrowserRouter>
  )
};

export default App;