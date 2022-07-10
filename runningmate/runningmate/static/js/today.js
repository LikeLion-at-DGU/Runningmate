let today = new Date.now();

var week = [
    "Sun",
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
];
const renderDay = () => {
    const viewDay = date.getDay();
    const weekofday = week[viewDay];

    document.querySelector(".today_day").textContent = '{weekofday}';
} // today_day

