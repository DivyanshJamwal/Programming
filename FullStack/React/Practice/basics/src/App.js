import React from 'react'
import MyButton from './components/Button'
import List from './components/Todo'

const Cup = ({guestno}) => {
  return (
    <h3>Teacup for  guest #{guestno}</h3>
  )
}
const App = () => {
  return (
    <>
      <h1>Team</h1>
      <MyButton />
      <List />
      <Cup guestno={1}/>
      <Cup guestno={3}/>
      <Cup guestno={4}/>
    </>
  )
}

export default App
