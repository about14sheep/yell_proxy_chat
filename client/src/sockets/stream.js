import { io } from 'socket.io-client'
import { socketUrl } from '../config'
import store from '../store'

export default class StreamSocket {

  constructor() {
    this.ws = io(`${socketUrl}/stream`)
    this.configureResponseHandlers()
  }

  configureResponseHandlers() {
    this.ws.on('stream_connect', res => {
      console.log(res['data'])
    })

    this.ws.on('stream_yell', res => {
      store.dispatch(this.addChatMessage(res['data']))
    })

    this.ws.on('new_emote', res => {
      console.log(res['data'])
    })

    this.ws.on('totem_join', res => {
      store.dispatch(this.setActiveRoom(res['data']))
    })

    this.ws.on('totem_leave', _ => {
      store.dispatch(this.clearActiveRoom())
    })
  }

  addChatMessage(msg) {
    return {
      type: 'CHAT_MESSAGE',
      msg
    }
  }

  setActiveRoom(totem) {
    return {
      type: 'SET_CHANNEL',
      totem
    }
  }

  clearActiveRoom() {
    return {
      type: 'CLEAR_CHANNEL'
    }
  }

  joinTotemRoom(userID, totemID) {
    this.ws.emit('totem_join', { user_id: userID, totem_id: totemID })
  }

  leaveTotemRoom(userID, totemID) {
    this.ws.emit('totem_leave', { user_id: userID, totem_id: totemID })
  }

  sendYell(username, userID, totemID, emoteID, text) {
    this.ws.emit('stream_yell', { user_id: userID, totem_id: totemID, username: username, text: text, emote_id: emoteID })
  }

  closeRoom(totemID) {
    this.ws.emit('close_room', {'totem_id': totemID})
  }
}