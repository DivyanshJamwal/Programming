import React from 'react'
import SmallBox from './SmallBox'
import './Sb_parent.css'

const Sb_parent = () => {
  const data = []

  for(let i = 0; i<100; i++){
    data.push(i+1)
  }

//   const children = []

//   data.forEach((num)=>{
//     children.push(<SmallBox num={num} />)
//   })
  
    return (
    <>
    <div id='parent-container'>
    {/* {children} */}
    {
        data.map((num)=>{
            return <SmallBox num={num} key={num} />
        })
    }
    </div>
    </>
    )
}

export default Sb_parent
