import React, { useState } from 'react'
import { useSelector } from 'react-redux'
import { streamSocket } from '../app'

import Message from './message'

function Channel(props) {
  const [text, setText] = useState('')
  const user = props.user
  const active_channel = props.channel
  const chatMessages = useSelector(state => state.streamReducer.chat)
  const chatStyle = {
    overflowY: 'scroll',
    height: '400px',
    width: '250px',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-end'
    
  }

  const leaveButtonPressed = _ => {
    streamSocket.leaveTotemRoom(user.id, active_channel.totem_id)
  }
  
  const sendYell = e => {
    e.preventDefault()
    streamSocket.sendYell(user.username, user.id, active_channel.totem_id, active_channel.emote.emote_id, text)
    setText('')
  }

  return (
    <>
      <h4>{`Totem ID: ${active_channel.totem_id}`}</h4>
      <button onClick={leaveButtonPressed}>Leave</button>
      <div style={chatStyle}>
        {chatMessages.map((el, i) => <Message key={i} msg={el} />)}
      </div>
      <form onSubmit={sendYell}>
        <input type='text' value={text} placeholder='Send a Message' onChange={e => setText(e.target.value)} />
        <input type='submit' />
      </form>
    </>
  )
}

export default Channel