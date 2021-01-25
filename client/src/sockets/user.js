import { io } from 'socket.io-client'
import { socketUrl } from '../config'

export default class UserSocket {
  constructor() {
    this.ws = io(`${socketUrl}/user`)
    this.configureResponseHandlers()

  }

  configureResponseHandlers() {
    this.ws.on('user_connect', res => {
      console.log(res['data'])
    })

    this.ws.on('user_save', res => {
      console.log(res['data'])
    })

    this.ws.on('get_user', res => {
      console.log(res['data'])
    })

    this.ws.on('user_location', res => {
      console.log(res['data'])
    })

    this.ws.on('emote_created', res => {
      console.log(res['data'])
    })
  }

  saveUserHash(userID, username) {
    this.ws.emit('user_save', { user_id: userID, username: username })
  }

  getUserHash(id) {
    this.ws.emit('user_get', { user_id: id })
  }

  updateUserLocation(long, lat, id) {
    this.ws.emit('user_location', { longitude: long, latitude: lat, user_id: id })
  }

  createEmote(emoteID, imageURL, userID) {
    this.ws.emit('create_emote', { emote_id: emoteID, image_url: imageURL, user_id: userID })
  }

}