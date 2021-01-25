const totemReducer = (state={}, action) => {
  switch(action.type) {
    case 'SET_TOTEMS': {
      return {
        ...state,
        totems: action.totems
      }
    }

    default: return state
  }
}

export default totemReducer