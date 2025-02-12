import React from 'react'
import './MonthYear.css'

// Month and Year Display
function MonthYear({ currentMonth, currentYear }) {
  return (
    <div className="month-year">
        <div className="month">{currentMonth}</div>
        <div className="year">{currentYear}</div>
    </div>
  )
}

export default MonthYear