import React, { useState } from 'react'
import { useSelector } from 'react-redux'
import { streamSocket } from '../app'

function Channel(props) {
  const [text, setText] = useState('')
  const user = props.user
  const active_channel = useSelector(state => state.totemReducer.active_channel)

  const leaveButtonPressed = _ => {
    if (active_channel) {
      streamSocket.leaveTotemRoom(user.id, active_channel.totem_id)
    }
  }

  const sendYell = e => {
    e.preventDefault()
    streamSocket.sendYell(user.username, user.id, active_channel.totem_id, active_channel.emote.emote_id, text)
  }

  return (
    <>
      <h4>{`Totem ID: ${active_channel.totem_id}`}</h4>
      <button onClick={leaveButtonPressed}>Leave</button>
      <form onSubmit={sendYell}>
        <input type='text' placeholder='Send a Message' onChange={e => setText(e.target.value)} />
        <input type='submit' />
      </form>
    </>
  )
}

export default Channel