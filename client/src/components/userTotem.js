import React from 'react'
import { totemSocket, streamSocket } from '../app'

function UserTotem({ userID, totem }) {

  const createButton = _ => {
    if (totem.isActive == 1) {
      return <button onClick={handleTotemPickup}>Pickup Totem</button>
    }
    return <button onClick={handleTotemPlace}>Place Totem</button>
  }
  
  const handleTotemPlace = _ => {
    navigator.geolocation.getCurrentPosition(pos => {
      totemSocket.saveTotemHash(userID, totem.totem_id, totem.skin.totem_skin_id, totem.emote.emote_id)
      totemSocket.placeTotem(pos.coords.longitude, pos.coords.latitude, userID)
    })
  }

  const handleTotemPickup = _ => {
    totemSocket.pickupTotem(totem.totem_id)
    streamSocket.closeRoom(totem.totem_id)
  }

  return (
    <>
      <p>User: {totem.owner.username}</p>
      <p>Discovery Emote: {totem.emote.image_url}</p>
      <p>Totem Skin: {totem.skin.image_url}</p>
      {createButton()}
    </>
  )

}

export default UserTotem