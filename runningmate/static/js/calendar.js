// Date 객체 생성
let date = new Date();//오늘 날짜 
var monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];
const renderCalendar = () => {
  const viewYear = date.getFullYear();
  const viewMonth = date.getMonth();

  // year-month 채우기
  document.querySelector('.year-month').textContent = `${viewYear}년 ${viewMonth + 1}월`;

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
    nextDates.push(i)
  }

  // Dates 합치기
  const dates = prevDates.concat(thisDates, nextDates);

  // Dates 정리
  const firstDateIndex = dates.indexOf(1);
  const lastDateIndex = dates.lastIndexOf(TLDate);
  dates.forEach((date, i) => {
    const condition = i >= firstDateIndex && i < lastDateIndex + 1
                      ? 'this'
                      : 'other';

    dates[i] = `<div class="date"><span class="${condition}">${date}</span></div>`;
  })


  // Dates 그리기
  document.querySelector('.dates').innerHTML = dates.join('');
}

renderCalendar();

const prevMonth = () => {
  date.setDate(1);
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
}

const nextMonth = () => {
  date.setDate(1);
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
}

const goToday = () => {
  date = new Date();
  renderCalendar();
}

const today = new Date();
if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
  for (let date of document.querySelectorAll('.this')) {
    if (+date.innerText === today.getDate()) {
      date.classList.add('today');
      break;
    }
  }
}

const calendarDates = document.querySelectorAll(".date")
const eventTypes = ["focus", "click"]

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + "=")) {
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
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
  beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
  }
});

function objectToJson(object) {
  const object_to_string = JSON.stringify(object);
  const string_to_json = JSON.parse(object_to_string);
  return string_to_json;
}

calendarDates.forEach((date) => {
  eventTypes.forEach((type) => {
      date.addEventListener(type, () => {
          const dateNum = date.childNodes[1].innerText
          $.ajax({
              type: "POST",
              url: "/showevent",
              data: JSON.stringify(dateNum),
              success: function (context) {
                  const object = objectToJson(context)
                  const status = object.status
                  if (status == "exist") {
                      const title1 = object.title1
                      const datetime1 = object.datetime1
                      schedule_1.innerHTML = "<p>" + title1 + "<br>" + datetime1 + "</p>"
                      const title2 = object.title2
                      const datetime2 = object.datetime2
                      schedule_2.innerHTML = "<p>" + title2 + "<br>" + datetime2 + "</p>"
                  } else {
                      schedule_1.innerHTML = "<p>오늘 할 일이 없습니다.</p>"
                      schedule_2.innerHTML = "<p>오늘 할 일이 없습니다.</p>"
                  }
              },
              error: function (xhr, errmsg, err) {
                  console.log(xhr.status + ": " + xhr.responseText + "\n\n" + errmsg + "\n\n" + err)
              }
          })
      })
  })
});