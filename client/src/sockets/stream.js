import { io } from 'socket.io-client'
import { socketUrl } from '../config'

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
      const data = res['data']
      console.log(`${data.username}: ${data.text}`)
    })

    this.ws.on('new_emote', res => {
      console.log(res['data'])
    })
  }

  sendYell(username, userID, totemID, emoteID, text) {
    this.ws.emit('stream_yell', { user_id: userID, totem_id: totemID, username: username, text: text, emote_id: emoteID })
  }
}