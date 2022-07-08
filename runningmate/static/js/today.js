  
const todayTime = () => {
    let now = new Date();
    const week = ['SUN', 'MON', 'TUE', 'WED', 'TUH', 'FRI', 'SAT'];
    let dayOfWeek = week[now.getDay()];

    // today-day 채우기
    document.querySelector('.today-day').textContent = `${dayOfWeek}`;

    return dayOfWeek
}