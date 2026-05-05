import React from 'react'
import './Navbar.css'
import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <>
    <nav>
    <div id='navbar-container'>
      <div>
        <span><b>TripKaro</b></span>
      </div>
      <div>
        <Link to={"/"}><span>Home</span></Link>
        <Link to={"/reservation"}><span>Reservation</span></Link>
        
      </div>
    </div>
    </nav>
    </>
  )
}

export default Navbar
