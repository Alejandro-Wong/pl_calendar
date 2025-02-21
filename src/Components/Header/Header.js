import React from 'react'
import MonthYear from '../MonthYear/MonthYear.js';
import Navigation from '../Navigation/Navigation.js';
// import Week from '../Week/Week.js';
import './Header.css'

function Header({ currentMonth, currentYear, todaysDate, monthIdx, setMonth, totalMonthPl }) {
  return (
    <div className="header">
      <MonthYear currentMonth={currentMonth} currentYear={currentYear}/>
      {/* <div className="todaysDate">{todaysDate}</div> */}
      <div className="totalPl">Total Profit/Loss: 
        <span id="pl" style={{color: totalMonthPl > 0 ? 'green' : totalMonthPl < 0 ? 'red' : 'white'}}>${totalMonthPl}</span>
      </div>
      <Navigation monthIdx={monthIdx} setMonth={setMonth}/>
    </div>
  )
}

export default Header

