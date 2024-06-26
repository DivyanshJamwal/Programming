import React, { useState } from 'react'
import './Card.css'
const Card = ({item,price}) => {

    // let qty = 0

    const [qty,setQty] = useState(1)
    const add =()=>{
        console.log("Item Added")
        setQty(qty+1)
        // qty +=1
        console.log(qty)
    }
    const remove =()=>{
        console.log("Item Removed")
        setQty(qty-1)
        // qty -=1
        console.log(qty)
    }
    return (
    <>
    <div id='container'>
        <div className='head'>
            <p>{item}</p>
            <p>₹ {price}</p>
        </div>
        <p id='qty'>QTY : {qty}</p>
        <div className='btn'>
            <button onClick={add}>Add</button>
            <button onClick={remove}>Remove</button>
        </div>
    </div>
    </>
  )
}

export default Card
