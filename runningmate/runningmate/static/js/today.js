// let today = new Date.now();

// var week = [
//     "Sun",
//     "Mon",
//     "Tue",
//     "Wed",
//     "Thu",
//     "Fri",
//     "Sat",
// ];
// const renderDay = () => {
//     const viewDay = date.getDay();
//     const weekofday = week[viewDay];

//     document.querySelector(".today_day").textContent = '{weekofday}';
// } // today_day


const today1 = new Date();

const year = today1.getFullYear();
const month = today1.getMonth() + 1;
const day = today1.getDate();
var week = [
    "SUNDAY",
    "MONDAY",
    "TUESDAY",
    "WEDENSDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
];

document.querySelector(".day_week").innerHTML = week[today1.getDay()];
document.querySelector(".date_week").innerHTML = year + '.' + month + '.' + day;