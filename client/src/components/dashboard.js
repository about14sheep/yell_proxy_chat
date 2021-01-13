import React from 'react';
import { useSelector } from 'react-redux';

function Dashboard() {
  const user = useSelector(state => state.authReducer.user)
  return (
    <h1>{user.username}'s Dashboard</h1>
  )
}

export default Dashboard;