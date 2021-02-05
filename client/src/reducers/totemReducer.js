const totemReducer = (state = {}, action) => {
  switch (action.type) {
    case 'SET_TOTEMS': {
      return {
        ...state,
        totems: action.totems
      }
    }

    case 'SET_CHANNEL': {
      return {
        ...state,
        active_channel: action.totem
      }
    }

    case 'CLEAR_CHANNEL': {
      const nextState = { ...state }
      delete nextState.active_channel
      return nextState
    }

    default: return state
  }
}

export default totemReducer