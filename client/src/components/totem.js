import React from 'react'
import { useSelector } from 'react-redux'
import { streamSocket } from '../app'

function Totem(props) {
  const totem = props.totem
  const active_channel = useSelector(state => state.streamReducer.totem)
  

  const joinButtonPressed = _ => {
    if (active_channel) {
      if (active_channel) {
        streamSocket.leaveTotemRoom(props.userID, active_channel.totem_id)
      }
    }
    streamSocket.joinTotemRoom(props.userID, totem.totem_id)
  }
  
  return (
    <>
      <h4>Owner: {totem.owner.username}</h4>
      <p>Discover Emote: {totem.emote.image_url}</p>
      <p>Totem Skin: {totem.skin.image_url}</p>
      <button onClick={joinButtonPressed}>Join</button>
    </>
  )
}

export default Totem