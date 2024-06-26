import React from 'react'
import './Hero.css'
const Hero = () => {
  return (
    <div class="hero-image">
        <div class="container">
          <h1>Welcome to TripKaro</h1>
          <p class="hero-sub">Explore the world with fantastic places to venture around</p>
          <input class="hero-search" placeholder="Search a City"/>    
        </div>
    </div>
  )
}

export default Hero
