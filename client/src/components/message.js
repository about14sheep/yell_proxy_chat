import React from 'react'

function Message(props) {
  const msg = props.msg
  const msgStyle = {
    bottom: '0',
    left: '0'
  }

  return (
    <>
      <div>{msg.username}: {msg.text}</div>
    </>
  )
}

export default Message