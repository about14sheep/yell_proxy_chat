import React from 'react'
import { useSelector } from 'react-redux'

function User(props) {
  const user = props.user


  return (
    <>
      <h2>Current User: {user.username}</h2>
    </>
  )
}

export default User