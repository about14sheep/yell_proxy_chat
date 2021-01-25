import { combineReducers } from 'redux';
import authReducer from './authReducer';
import totemReducer from './totemReducer'

const rootReducer = combineReducers({
  authReducer,
  totemReducer
});

export default rootReducer;