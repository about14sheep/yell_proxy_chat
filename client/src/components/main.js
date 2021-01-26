import React from 'react'
import { useSelector } from 'react-redux'

import Totem from './totem'

function Main() {
  const totems = useSelector(state => state.totemReducer.totems)
  const user = useSelector(state => state.authReducer.user)

  return (
    <>
      <h1>welcome to yell</h1>
      {totems ? totems.map(el => <Totem totem={el} userID={user.id} key={el.totem_id} />) : <h3>Loading Totems</h3>}
    </>
  )
}

export default Main;