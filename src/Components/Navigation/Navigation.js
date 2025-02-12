import React from 'react'
import './Navigation.css'


function Navigation({monthIdx, setMonth}) {

  const handlePrev = () => {
    setMonth(monthIdx - 1)
  };

  const handleNext = () => {
    setMonth(monthIdx + 1)
  };

  return (
    <div className="navContainer">
      <button className="navButton" id="prev" onClick={handlePrev}>Previous</button>
      <button className="navButton" id="next" onClick={handleNext}>Next</button>
    </div>
  )
}

export default Navigation