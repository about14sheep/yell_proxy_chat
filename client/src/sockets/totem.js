import { io } from 'socket.io-client'
import { socketUrl } from '../config'
export default class TotemSocket {

  constructor() {
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

    this.ws.on('totem_skin_save', res => {
      console.log(res['data'])
    })
  }

  saveTotemHash(ownerID, totemID, totemSkinID, emoteID) {
    this.ws.emit('totem_save', { owner_id: ownerID, totem_id: totemID, totem_skin_id: totemSkinID, emote_id: emoteID })
  }

  getTotemHash(id) {
    this.ws.emit('totem_get', { totem_id: id })
  }

  placeTotem(long, lat, id) {
    this.ws.emit('totem_place', { longitude: long, latitude: lat, totem_id: id })
  }

  getTotemsInRadius(long, lat, rad) {
    this.ws.emit('totem_scan', { longitude: long, latitude: lat, radius: rad })
  }

  joinTotemRoom(userID, totemID) {
    this.ws.emit('totem_join', { user_id: userID, totem_id: totemID })
  }

  leaveTotemRoom(userID, totemID) {
    this.ws.emit('totem_leave', { user_id: userID, totem_id: totemID })
  }

  saveTotemSkin(totemSkinID, imageURL, title) {
    this.ws.emit('totem_skin_save', { totem_skin_id: totemSkinID, image_url: imageURL, totem_title: title })
  }
}