import { combineReducers } from 'redux';
import authReducer from './auth_reducer';

const rootReducer = combineReducers({
  authReducer
});

export default rootReducer;