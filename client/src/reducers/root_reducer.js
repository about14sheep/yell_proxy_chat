import { combineReducers } from 'redux';
import authReducer from './authReducer';
import totemReducer from './totemReducer';
import streamReducer from './streamReducer'

const rootReducer = combineReducers({
  authReducer,
  totemReducer,
  streamReducer
});

export default rootReducer;