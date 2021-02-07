import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { Redirect, useHistory } from 'react-router-dom';

import { login } from '../actions/auth';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const dispatch = useDispatch();
  const history = useHistory()

  const handleSubmit = e => {
    e.preventDefault();
    dispatch(login(email, password));
    history.push('/')
  };

  return (
    <>
      <h2>Log in to Yell</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <input type='text' placeholder='Email' name='email' onChange={e => setEmail(e.target.value)} />
        </div>
        <div>
          <input type='text' placeholder='Password' name='email' onChange={e => setPassword(e.target.value)} />
        </div>
        <div>
          <input type='submit' />
        </div>
      </form>
    </>
  )
}

export default Login;