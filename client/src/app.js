import React, { useEffect, useState } from 'react';
import { BrowserRouter, Redirect, Route, Switch } from 'react-router-dom'

import Main from './components/main';
import Login from './components/login';
import Dashboard from './components/dashboard';
import UserSocket from './sockets/user'
import StreamSocket from './sockets/stream'
import TotemSocket from './sockets/totem'


import { loadToken, loadUser } from './actions/auth';
import { useDispatch, useSelector } from 'react-redux';

const PrivateRoute = ({ component: Component, ...rest }) => (
  <Route {...rest} render={props => (
    rest.needLogin === true ? <Redirect to='/login' /> : <Component {...props} />
  )} />
)

export const userSocket = new UserSocket()
export const totemSocket = new TotemSocket()

totemSocket.getTotemsInRadius(-86.767960, 36.174465, 2)
userSocket.updateUserLocation(-86.767960, 36.174465, 1)
userSocket.updateUserLocation(-86.767960, 36.174465, 2)


function App() {
  const [loaded, setLoaded] = useState(false)
  const needLogin = useSelector(state => !state.authReducer.token)
  const dispatch = useDispatch()

  useEffect(_ => {
    dispatch(loadToken())
    dispatch(loadUser())
    setLoaded(true)
  }, [dispatch])

  if (!loaded) return null;

  return (
    <BrowserRouter>
      <Switch>
        <PrivateRoute exact={true} path='/dashboard' needLogin={needLogin} component={Dashboard} />
        <Route exact={true} path='/'>
          <Main />
        </Route>
        <Route exact={true} path='/login'>
          <Login />
        </Route>
      </Switch>
    </BrowserRouter>
  )
};

export default App;