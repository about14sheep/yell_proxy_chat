import React, { useState } from 'react';
import { useDispatch } from 'react-redux';

import { login } from '../actions/auth';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const dispatch = useDispatch();

  const handleSubmit = e => {
    e.preventDefault();
    dispatch(login(email, password));
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input type='text' placeholder='Email' name='email' onChange={e => setEmail(e.target.value)} />
        <input type='text' placeholder='Password' name='email' onChange={e => setPassword(e.target.value)} />
        <input type='submit' />
      </form>
    </>
  )
}

export default Login;