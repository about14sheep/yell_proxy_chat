import React from 'react';
import { BrowserRouter, Redirect, Route, Switch } from 'react-router-dom'

import Main from './components/main' 

const PivateRoute = ({component: Component, ...rest}) => (
  <Route {...rest} render={props => (
    rest.needLogin === true ? <Redirect to='/login' /> : <Component {...props} />
  )} />
)


function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path='/'>
          <Main />
        </Route>
      </Switch>
    </BrowserRouter>
  )
};

export default App;