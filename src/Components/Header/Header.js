import React from 'react'
import MonthYear from '../MonthYear/MonthYear.js';
import Navigation from '../Navigation/Navigation.js';
// import Week from '../Week/Week.js';
import './Header.css'

function Header({ currentMonth, currentYear, todaysDate, monthIdx, setMonth }) {
  return (
    <div className="header">
      <MonthYear currentMonth={currentMonth} currentYear={currentYear}/>
      <div className="todaysDate">{todaysDate}</div>
      <Navigation monthIdx={monthIdx} setMonth={setMonth}/>
    </div>
  )
}

export default Header

