// Date 객체 생성
let date = new Date(); //오늘 날짜
var monthNames = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];
const renderCalendar = () => {
  const viewYear = date.getFullYear();
  const viewMonth = date.getMonth();

  // year-month 채우기
  document.querySelector(".year-month").textContent = `${viewYear}년 ${viewMonth + 1
    }월`;

  // 지난 달 마지막 Date, 이번 달 마지막 Date
  const prevLast = new Date(viewYear, viewMonth, 0);
  const thisLast = new Date(viewYear, viewMonth + 1, 0);

  const PLDate = prevLast.getDate();
  const PLDay = prevLast.getDay();

  const TLDate = thisLast.getDate();
  const TLDay = thisLast.getDay();

  // Dates 기본 배열들
  const prevDates = [];
  const thisDates = [...Array(TLDate + 1).keys()].slice(1);
  const nextDates = [];

  // prevDates 계산
  if (PLDay !== 6) {
    for (let i = 0; i < PLDay + 1; i++) {
      prevDates.unshift(PLDate - i);
    }
  }

  // nextDates 계산
  for (let i = 1; i < 7 - TLDay; i++) {
    nextDates.push(i);
  }

  // Dates 합치기
  const dates = prevDates.concat(thisDates, nextDates);

  // Dates 정리
  const firstDateIndex = dates.indexOf(1);
  const lastDateIndex = dates.lastIndexOf(TLDate);
  dates.forEach((date, i) => {
    const condition =
      i >= firstDateIndex && i < lastDateIndex + 1 ? "this" : "other";

    dates[
      i
    ] = `<div class="date"><span class="${condition}">${date}</span></div>`;
  });

  // Dates 그리기
  document.querySelector(".dates").innerHTML = dates.join("");
};

renderCalendar();

const prevMonth = () => {
  date.setDate(1);
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
};

const nextMonth = () => {
  date.setDate(1);
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
};

const goToday = () => {
  date = new Date();
  renderCalendar();
};




function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getCookie("csrftoken");
function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}
$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  },
});


function contextToJson(context) {
  const context_to_string = JSON.stringify(context);
  const string_to_json = JSON.parse(context_to_string);
  return string_to_json;
}
document.querySelectorAll(".date").forEach((date) => {
  date.addEventListener("click", () => {
    let dateNum = date.childNodes[0].innerText;
    $.ajax({
      type: "POST",
      url: "/showevent",
      data: JSON.stringify(dateNum),
      success: function (context) {
        let object = contextToJson(context);
        let status = object.status;
        if (status == "exist1" || status == "exist2") {
          /*데이터베이스 받아오기*/
          let title1 = object.title1;
          let body1 = object.body1;
          let starttime1 = object.starttime1;
          let endtime1 = object.endtime1;
          let place1 = object.place1;
          let color1 = object.color1;

          /*html에 영역 추가*/
          schedule_1.innerHTML = [
            "<div id = 'cal_sch1'>",
            "<section id = 'cal_title' ></section>",
            "<section id = cal_body></section>",
            "<section id = cal_time_place></section>",
            "</div>",
            "<div id = 'sch1_team'>",
            "<div class = 'cal_friend1' style=' background-color: {{calendar.0.color}};' id = 'sch1_team1' ></div>",
            "<div class = 'cal_friend1' style=' background-color: {{calendar.0.color}};' id = 'sch1_team2'></div>",
            "<div class = 'cal_friend1' style=' background-color: {{calendar.0.color}};' id = 'sch1_team3'></div>",
            "<div class = 'cal_friend1' style=' background-color: {{calendar.0.color}};' id = 'sch1_team4'></div>",
            "<div class = 'cal_friend1' style=' background-color: {{calendar.0.color}};' id = 'sch1_team5'></div>",
            "<div class = 'cal_friend1' style=' background-color: {{calendar.0.color}};' id = 'sch1_team6'></div>",
            "</div>",
          ].join("")


          /*html에 내용 추가*/
          cal_title.innerHTML = title1;
          cal_body.innerHTML = body1;
          cal_time_place.innerHTML = starttime1 + "~" + endtime1 + "/" + place1;

          /*제목 색 css 변경 (과목 색이랑 같게) */
          cal_title.style.color = color1;

          /*미모지 css 변경 추가*/
          sch1_team1.style.backgroundColor = color1;
          sch1_team2.style.backgroundColor = color1;
          sch1_team3.style.backgroundColor = color1;
          sch1_team4.style.backgroundColor = color1;
          sch1_team5.style.backgroundColor = color1;
          sch1_team6.style.backgroundColor = color1;
          sch1_team1.style.marginRight = '5px';
          sch1_team2.style.marginRight = '5px';
          sch1_team3.style.marginRight = '5px';
          sch1_team4.style.marginRight = '5px';
          sch1_team5.style.marginRight = '5px';
          sch1_team6.style.marginRight = '5px';

        }

        else {
          schedule_1.innerHTML = "<div id = 'no_schedule'>아직 등록된 일정이 없어요</div>";
        }
      },
      error: function (xhr, errmsg, err) {
        console.log(
          xhr.status + ": " + xhr.responseText
        );
      },
    });
  });
});





const today = new Date();
if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
  for (let date of document.querySelectorAll(".this")) {
    if (+date.innerText === today.getDate()) {
      date.classList.add("today");
      break;
    }
  }
}

