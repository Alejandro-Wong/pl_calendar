import React, { useState, useEffect } from 'react';
import Header from '../Header/Header.js';
import Week from '../Week/Week.js';
import Calendar from '../Calendar/Calendar.js';
import './App.css';

// Months
const months = ['January', 'February', 'March', 'April', 'May',
  'June', 'July', 'August', 'September', 'October',
  'November', 'December']

function App() {

  // State Initializations
  const [monthIdx, setMonthIdx] = useState(new Date().getMonth());
  const [yearIdx, setYearIdx] = useState(new Date().getFullYear());
  const [plData, setPlData] = useState([{}]);
  const currentMonth = months[monthIdx];
  const currentYear = yearIdx;
  const todaysDate = new Date().toDateString()

  // Fetch Profit/Loss Data

  // From Flask
  // useEffect(() => {
  //   fetch("/profit_loss").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       setPlData(data)
  //       console.log(data)
  //     }
  //   )
  // }, []);

  // From Postgres
  useEffect(() => {
    fetch("/pl_calendar").then(
      res => res.json()
    ).then(
      data => {
        setPlData(data)
        // console.log(data)
      }
    )
  }, []);

  // Loop Months, Increment/Decrement Years
  if (monthIdx < 0) {
    setMonthIdx(11);
    setYearIdx(yearIdx - 1);
  };

  if (monthIdx > 11) {
    setMonthIdx(0);
    setYearIdx(yearIdx + 1);
  }

  // Total Month's PL for Header
  const monthPl = [];
  for (let i = 0; i < plData.length; i++) {
    let month = new Date(plData[i].date).getMonth()
    if (months[month] === currentMonth) {
      monthPl.push(Number(plData[i].profit_loss))
    };
  };

  const totalMonthPl = monthPl.reduce((b, a) => b + a, 0).toFixed(2)

  return (
    <div className="App">
      <Header 
        currentMonth={currentMonth}
        currentYear={currentYear}
        totalMonthPl={totalMonthPl}
        todaysDate={todaysDate}
        monthIdx={monthIdx}
        setMonth={setMonthIdx}
      />
      <Week />
      <Calendar monthIdx={monthIdx} yearIdx={yearIdx} plData={plData}/>
    </div>
  );
}

export default App;
