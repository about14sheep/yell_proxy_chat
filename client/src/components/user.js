import React from 'react'
import { useSelector } from 'react-redux'
import { totemSocket } from '../app'
import UserTotem from './userTotem'

function User(props) {
  const user = props.user
  const totem = useSelector(state => state.totemReducer.userTotem)

  if (!totem) {
    totemSocket.getUserTotem(user.user_totem_id[0].id)
  }

  return (
    <>
      <h2>Current User: {user.username}</h2>
      <div>
        <h3>Your Totem: </h3>
        {totem ? <UserTotem totem={totem} userID={user.id} /> : null}
      </div>
    </>
  )
}

export default User