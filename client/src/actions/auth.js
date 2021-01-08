import { apiUrl } from '../config';

const setUser = user => ({
  type: 'SET_USER',
  user
})

export const login = (email, password) => async dispatch => {
  const res = await fetch(`${apiUrl}/session`, {
    method: 'PUT',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({email, password})
  });

  if (res.ok) {
    const user = await res.json();
    dispatch(setUser(user));
    console.log(user);
  }
}