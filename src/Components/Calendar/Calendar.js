import React from 'react'
import Day from '../Day/Day.js';
import './Calendar.css'
function Calendar({ monthIdx, yearIdx, plData }) {

  // Convert array of objects (plData) into single object
  let plObj = {};
  for (let i = 0; i < plData.length; i++) {
    plObj[plData[i].date] = plData[i].profit_loss;
  };


  // Calendar Template (5 rows 7 Columns)
  const days = [
          '','','','','','','',
          '','','','','','','',
          '','','','','','','',
          '','','','','','','',
          '','','','','','','',
  ];


  // Month and Year Indexes
  const month = monthIdx;
  const year = yearIdx;

  const daysInMonth = new Date(year, month + 1, 0).getDate(); // Total number of days depending on month
  const firstDayOfMonth = new Date(year, month, 1);
  const firstDayIdx = firstDayOfMonth.getDay();
  const currentDay = new Date().toISOString().split('T')[0];
  

  // Populate calendar with correct number of days and numbers in correct spots
  for (let i=firstDayIdx, j=1; i<daysInMonth + firstDayIdx; i++, j++){
    days[i] = j;
  };


  // Create Day components in correct positions
  const calDays = [];
  for (let i=0; i<days.length; i++) {
    let date = days[i] ? new Date(year,month,days[i]).toISOString().split('T')[0] : ''
    let pl = Number(plObj[date]);
    console.log(typeof pl)
    calDays.push(<Day index={i} dayNum={days[i]} date={date} currentDay={currentDay} plData={pl}/>);
  };

  return (
        <div className="calFrame">
          {calDays}
        </div>
    )
}

export default Calendar