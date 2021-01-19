import { socketUrl } from '../config'

export default class StreamSocket {

  constructor(io) {
    this.ws = io(`${socketUrl}/stream`)
    this.configureResponseHandlers()
  }

  configureResponseHandlers() {
    this.ws.on('stream_connect', res => {
      console.log(res['data'])
    })

    this.ws.on('stream_yell', res => {
      console.log(res['data'])
    })
  }
}