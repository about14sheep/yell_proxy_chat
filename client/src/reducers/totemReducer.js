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

    case 'USER_TOTEM_PLACED': {
      const nextState = { ...state }
      nextState.userTotem.isActive = true
      return nextState
    }

    default: return state
  }
}

export default totemReducer