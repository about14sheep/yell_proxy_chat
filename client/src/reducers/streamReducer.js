const streamReducer = (state = { }, action) => {
  switch (action.type) {
    case 'SET_CHANNEL': {
      return {
        ...state,
        totem: action.totem,
        chat: []
      }
    }

    case 'REMOVE_TOTEM': {
      if (state.totem.totem_id === action.id) {
        const nextState = { ...state }
        delete nextState.totem
        delete nextState.chat
        return nextState
      }
    }

    case 'CHAT_MESSAGE': {
      return {
        ...state,
        chat: [...state.chat, action.msg]
      }
    }

    case 'REMOVE_TOTEMS': {
      const nextState = { ...state }
      delete nextState.totem
      delete nextState.chat
      return nextState
    } 

    case 'CLEAR_CHANNEL': {
      const nextState = { ...state }
      delete nextState.totem
      delete nextState.chat
      return nextState
    }

    default: return state
  }
}

export default streamReducer