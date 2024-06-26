import React from 'react'
import Card from './Card'
import './Cards.css'

const Cards = () => {
  return (
    <><div id='parent-container'>
      <Card item="iPhone" price="64K"/>
      <Card item="Airpods" price="22K"/>
      <Card item="Macbook" price="120K"/>
      <Card item="iPad" price="79K"/>
      </div>
    </>
  )
}

export default Cards
