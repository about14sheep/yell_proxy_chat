import {
  SET_USER,
  REMOVE_USER,
  SET_TOKEN,
  REMOVE_TOKEN
} from '../actions/auth'

const authReducer = (state={}, action) => {
  switch (action.type) {
    case SET_USER: {
      return {
        ...state,
        user: action.user
      };
    };

    case REMOVE_USER: {
      const nextState = {...state};
      delete nextState.user;
      return nextState;
    };

    case SET_TOKEN: {
      return {
        ...state,
        token: action.token
      };
    };

    case REMOVE_TOKEN: {
      const nextState = {...state};
      delete nextState.token;
      return nextState;
    };

    default: return state;
  };
};

export default authReducer;