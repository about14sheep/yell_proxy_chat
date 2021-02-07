import React from 'react'
import { useSelector } from 'react-redux'
import { totemSocket } from '../app'
import { userSocket } from '../app'

import Totem from './totem'
import Channel from './channel'
import User from './user'

const mainStyle = {
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'space-evenly'
}

function Main() {
  const totems = useSelector(state => state.totemReducer.totems)
  const user = useSelector(state => state.authReducer.user)
  const aChannel = useSelector(state => state.streamReducer.totem)

  if (!totems) {
    navigator.geolocation.getCurrentPosition(pos => {
      totemSocket.getTotemsInRadius(pos.coords.longitude, pos.coords.latitude, 2)
      if (!user.haveLocation) {
        userSocket.saveUserHash(user.id, user.username)
        userSocket.updateUserLocation(pos.coords.longitude, pos.coords.latitude, user.id)
      }
    })
  }

  return (
    <>
      <div style={mainStyle}>
        <div>
          <h1>welcome to yell</h1>
          <User user={user} />
        </div>
        <div>
          <h2>Totems in range (2 mi)</h2>
          {totems ? totems.map(el => <Totem totem={el} userID={user.id} key={el.totem_id} />) : <h3>Loading Totems...</h3>}
        </div>
        <div>
          {aChannel ? <Channel channel={aChannel} user={user} /> : <h3>join a channel to chat!</h3>}
        </div>
      </div>
    </>
  )
}

export default Main;