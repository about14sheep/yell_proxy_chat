import React from 'react'

function Message(props) {
  const msg = props.msg
  
  return (
    <>
      <div>{msg.username}: {msg.text}</div>
    </>
  )
}

export default Message