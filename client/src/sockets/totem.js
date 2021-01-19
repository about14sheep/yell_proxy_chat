import { socketUrl } from '../config'

export default class TotemSocket {

  constructor(io) {
    this.ws = io(`${socketUrl}/totem`)
    this.configureResponseHandlers()
  }
  
  configureResponseHandlers() {
    this.ws.on('totem_connect', res => {
      console.log(res['data'])
    })

    this.ws.on('get_totem', res => {
      console.log(res['data'])
    })

    this.ws.on('totems_near', res => {
      console.log(res['data'])
    })

    this.ws.on('totem_save', res => {
      console.log(res['data'])
    })

    this.ws.on('totem_place', res => {
      console.log(res['data'])
    })

    this.ws.on('totem_join', res => {
      console.log(res['data'])
    })

    this.ws.on('totem_leave', res => {
      console.log(res['data'])
    })
  }
}