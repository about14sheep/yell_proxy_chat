import React from 'react'

function Totem(props) {
  const totem = props.totem
  return (
    <>
      <h4>Owner: {totem.owner.username}</h4>
      <p>Discover Emote: {totem.emote.image_url}</p>
      <p>Totem Skin: {totem.skin.image_url}</p>
    </>
  )
}

export default Totem