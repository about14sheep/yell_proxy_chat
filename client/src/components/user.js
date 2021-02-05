import React from 'react'
import { useSelector } from 'react-redux'
import { userSocket } from '../app'

function User() {
  const user = useSelector(state => state.authReducer.user)


  return (
    <>
      <h2>Current User: {user.username}</h2>
    </>
  )
}

export default User