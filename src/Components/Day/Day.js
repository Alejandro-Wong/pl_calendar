import React from 'react'
import './Day.css'
function Day({ index, dayNum, date, currentDay, plData}) {
  return (
    <div className="day"
        style={{border: currentDay === date ? '6px solid yellow;' : '1px solid darkgray',
                "background-color": plData > 10 ? 'rgba(0, 255, 0, 0.2)' 
                                  : plData < -10 ? 'rgba(255, 0, 0, 0.2)' : ''}}>
      <div className="index">{index}</div>
      <div className="dayNum">{dayNum}</div>
      <div className="date">{date}</div>
      <div className="plData">{plData ? plData : ''}</div>
    </div>
  )
}

export default Day