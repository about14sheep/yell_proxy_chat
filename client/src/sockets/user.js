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
}