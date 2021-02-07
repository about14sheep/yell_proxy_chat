import React from 'react'
import { totemSocket } from '../app'

function UserTotem({ userID, totem }) {
  
  const handleTotemPlace = _ => {
    navigator.geolocation.getCurrentPosition(pos => {
      totemSocket.saveTotemHash(userID, totem.totem_id, totem.skin.totem_skin_id, totem.emote.emote_id)
      totemSocket.placeTotem(pos.coords.longitude, pos.coords.latitude, userID)
    })
  }

  return (
    <>
      <p>User: {totem.owner.username}</p>
      <p>Discovery Emote: {totem.emote.image_url}</p>
      <p>Totem Skin: {totem.skin.image_url}</p>
      {totem.isActive ? <button onClick={handleTotemPlace}>Place Totem</button> : null}
    </>
  )

}

export default UserTotem