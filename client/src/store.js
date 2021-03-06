import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';

import rootReducer from './reducers/root_reducer'

const configureStore = _ => {
  return createStore(
    rootReducer,
    applyMiddleware(thunk)
  )
};

const store = configureStore()
export default store