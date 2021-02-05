const streamReducer = (state = {chat: []}, action) => {
  switch (action.type) {
    case 'SET_CHANNEL': {
      return {
        ...state,
        totem: action.totem
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
      nextState.chat = []
      return nextState
    }

    default: return state
  }
}

export default streamReducer