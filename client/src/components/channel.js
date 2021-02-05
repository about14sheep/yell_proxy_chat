import React from 'react'
import { useSelector } from 'react-redux'
import { totemSocket } from '../app'

function Channel(props) {
  const roomID = props.totemID
  const user = props.user
  const active_channel = useSelector(state => state.totemReducer.active_channel)

  const leaveButtonPressed = _ => {
    if (active_channel) {
      totemSocket.leaveTotemRoom(user.id, active_channel)
    }
  }

  const sendYell = _ => {
    totemSocket.sendYell(user.username, user.id, roomID, 1, 'this is a testie')
  }

  return (
    <>
      <h4>{`Totem ID: ${roomID}`}</h4>
      <button onClick={leaveButtonPressed}>Leave</button>
      <button onClick={sendYell}>Test</button>
    </>
  )
}

export default Channel