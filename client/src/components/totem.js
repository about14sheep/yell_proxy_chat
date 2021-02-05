import React from 'react'
import { streamSocket } from '../app'

function Totem(props) {
  const totem = props.totem
  

  const joinButtonPressed = _ => {
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