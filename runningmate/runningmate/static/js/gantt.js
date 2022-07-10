function createChart(e) {
    const days = document.querySelectorAll(".chart-values li");
    const tasks = document.querySelectorAll(".chart-bars li");
    const daysArray = [...days];    // NodeList(유사배열) -> 아래 filter 기능 쓰기 위해 순수배열로 변경

    // chart-bars li 각각마다 할 일(task) 지정
    tasks.forEach(el => {
        // 변수 지정
        const duration = el.dataset.duration.split("-");
        // el.setAttribute("data-duration", getDay(duration[0]) + "-" + getDay(duration[1]))
        const startDay = duration[0]
        const endDay = duration[1]
        let left = 0,   // 해당 화살표 함수 범위 내에서 변수 지정
            width = 0;

        // 시작일 left 확인 - 시작 요일 ½(절반) 유무 체크
        if (startDay.endsWith("½")) {
            const filteredArray = daysArray.filter(day => day.textContent == startDay.slice(0, -1)); // slice 이용 끝 ½만 자르고 li(day) 요소와 같은지 비교
            left = filteredArray[0].offsetLeft + filteredArray[0].offsetWidth / 2;
        } else {
            const filteredArray = daysArray.filter(day => day.textContent == startDay);
            left = filteredArray[0].offsetLeft;
        }

        // 바 width 확인
        if (endDay.endsWith("½")) {
            const filteredArray = daysArray.filter(day => day.textContent == endDay.slice(0, -1));
            width = filteredArray[0].offsetLeft + filteredArray[0].offsetWidth / 2 - left;
        } else {
            const filteredArray = daysArray.filter(day => day.textContent == endDay);
            width = filteredArray[0].offsetLeft + filteredArray[0].offsetWidth - left;
        }


        // apply css
        // left, width li css 지정
        el.style.left = `${left}px`;    // 과거 el.style.left = left +'px'와 동일
        el.style.width = `${width}px`;
        if (e.type == "load") {
            el.style.backgroundColor = el.dataset.color; // 막대 색 data-color 가져와서 지정
            el.style.opacity = 1; // load 발생 시 막대 생기게 지정
        }
    });
}


window.addEventListener("load", createChart);
window.addEventListener("resize", createChart);