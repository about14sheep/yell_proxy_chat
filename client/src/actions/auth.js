import { apiUrl } from '../config';

const TOKEN_KEY = 'yell/session/token';
const USER_KEY = 'yell/session/user';

export const SET_USER = 'SET_USER';
export const REMOVE_USER = 'REMOVE_USER';
export const SET_TOKEN = 'SET_TOKEN';
export const REMOVE_TOKEN = 'REMOVE_TOKEN';

const setUser = user => ({
  type: SET_USER,
  user
});

const removeUser = _ => ({
  type: REMOVE_USER
});

const setToken = token => ({
  type: SET_TOKEN,
  token
});

const removeToken = _ => ({
  type: REMOVE_TOKEN
});

export const loadToken = _ => async dispatch => {
  const token = window.localStorage.getItem(TOKEN_KEY);
  if (token) dispatch(setToken(token));
}

export const loadUser = _ => async dispatch => {
  const user = JSON.parse(window.localStorage.getItem(USER_KEY));
  if (user) dispatch(setUser(user));
}

export const login = (email, password) => async dispatch => {
  const res = await fetch(`${apiUrl}/session`, {
    method: 'PUT',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({email, password})
  });

  if (res.ok) {
    const {user, token} = await res.json();
    window.localStorage.setItem(TOKEN_KEY, token)
    window.localStorage.setItem(user, JSON.stringify(user));
    dispatch(setUser(user));
    dispatch(setToken(token));
  }
}

export const logout = userId => async dispatch => {
  const res = await fetch(`${apiUrl}/session`, {
    method: 'DELETE',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({'user_id': userId})
  });

  if (res.ok) {
    window.localStorage.removeItem(TOKEN_KEY);
    window.localStorage.removeItem(USER_KEY);
    dispatch(removeToken());
    dispatch(removeUser());
  }
}