const streamReducer = (state = { }, action) => {
  switch (action.type) {
    case 'SET_CHANNEL': {
      return {
        ...state,
        totem: action.totem,
        chat: []
      }
    }

    case 'CHAT_MESSAGE': {
      return {
        ...state,
        chat: [...state.chat, action.msg]
      }
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