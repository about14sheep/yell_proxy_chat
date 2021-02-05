import React from 'react'
import { useSelector } from 'react-redux'

import Totem from './totem'
import Channel from './channel'

function Main() {
  const totems = useSelector(state => state.totemReducer.totems)
  const user = useSelector(state => state.authReducer.user)
  const aChannel = useSelector(state => state.totemReducer.active_channel)

  return (
    <>
      <h1>welcome to yell</h1>
      {totems ? totems.map(el => <Totem totem={el} userID={user.id} key={el.totem_id} />) : <h3>Loading Totems</h3>}
      {aChannel ? <Channel totemID={aChannel} user={user} /> : <h3>join a channel to chat!</h3>}
    </>
  )
}

export default Main;