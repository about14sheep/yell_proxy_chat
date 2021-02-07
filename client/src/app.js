import React, { useEffect, useState } from 'react';
import { BrowserRouter, Redirect, Route, Switch, useLocation } from 'react-router-dom'

import Main from './components/main';
import Login from './components/login';
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

const ScrollToTop = _ => {
  const { pathname } = useLocation()
  useEffect(_ => {
    window.scroll(0, 0)
  }, [pathname])
  return null
}

export const userSocket = new UserSocket()
export const totemSocket = new TotemSocket()
export const streamSocket = new StreamSocket()



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
      <ScrollToTop />
      <Switch>
          <PrivateRoute exact={true} path='/' needLogin={needLogin} component={Main} />
          <Route exact={true} path='/login'>
            <Login />
          </Route>
      </Switch>
    </BrowserRouter>
  )
};

export default App;