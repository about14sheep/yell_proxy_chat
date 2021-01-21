import {socketUrl} from '../config'

export default class UserSocket {
  constructor(io) {
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
  }

  saveUserHash(userID, username) {
    this.ws.emit('user_save', {user_id: userID, username: username})
  }

  getUserHash(id) {
    this.ws.emit('user_get', {user_id: id})
  }

  updateUserLocation(long, lat, id) {
    this.ws.emit('user_location', {longitude: long, latitude: lat, user_id: id})
  }

}