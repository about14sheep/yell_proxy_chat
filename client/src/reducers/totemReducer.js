const totemReducer = (state = {}, action) => {
  switch (action.type) {
    case 'SET_TOTEMS': {
      return {
        ...state,
        totems: action.totems
      }
    }

    case 'SET_TOTEM': {
      return {
        ...state,
        totems: [...state.totems, action.totem]
      }
    }

    case 'SET_USER_TOTEM': {
      return {
        ...state,
        userTotem: action.totem
      }
    }

    case 'REMOVE_TOTEMS': {
      const nextState = { ...state }
      delete nextState.totems
      delete nextState.userTotem
      return nextState
    }

    case 'USER_TOTEM_PLACED': {
      return {
        ...state,
        totems: [...state.totems, action.totem],
        userTotem: action.totem
      }
    }

    default: return state
  }
}

export default totemReducer