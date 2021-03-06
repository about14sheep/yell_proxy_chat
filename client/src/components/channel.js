import React, { useState } from 'react'
import { useSelector } from 'react-redux'
import { streamSocket } from '../app'

import Message from './message'

function Channel(props) {
  const [text, setText] = useState('')
  const user = props.user
  const activeTotem = props.channel
  const chatMessages = useSelector(state => state.streamReducer.chat)
  const chatStyle = {
    overflowY: 'scroll',
    height: '400px',
    width: '250px',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-end'
  }

  const headerStyle = {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-evenly'
  }

  const leaveButtonPressed = _ => {
    streamSocket.leaveTotemRoom(user.id, activeTotem.totem_id)
  }
  
  const sendYell = e => {
    e.preventDefault()
    streamSocket.sendYell(user.username, user.id, activeTotem.totem_id, activeTotem.emote.emote_id, text)
    setText('')
  }

  return (
    <>
      <div style={headerStyle}>
        <h3>{`${activeTotem.owner.username}'s Totem`}</h3>
        <button onClick={leaveButtonPressed}>Leave</button>
      </div>
      <div style={chatStyle}>
        {chatMessages ? chatMessages.map((el, i) => <Message key={i} msg={el} />) : null}
      </div>
      <form onSubmit={sendYell}>
        <input type='text' value={text} placeholder='Send a Message' onChange={e => setText(e.target.value)} />
        <input type='submit' />
      </form>
    </>
  )
}

export default Channel