// 과목명 
document.getElementById("dday1_subject").innerHTML = "IT서비스관리"
document.getElementById("dday2_subject").innerHTML = "조직행위 03"
document.getElementById("dday3_subject").innerHTML = "파이썬과 경영"

//회의 주제
document.getElementById("dday1_meeting").innerHTML = "주제 선정 회의"
document.getElementById("dday2_meeting").innerHTML = "인터뷰 기업 선정 및 섭외"
document.getElementById("dday3_meeting").innerHTML = "그룹 스터디 2주차"

//디데이 계산 
var sub1_finalDay = new Date("2022-07-07:23:59:59+0900"); //dday 첫째 칸 마감일
var sub2_finalDay = new Date("2022-07-30:23:59:59+0900"); //dday 둘째 칸 마감일
var sub3_finalDay = new Date("2022-08-10:23:59:59+0900"); //dday 셋째칸 마감일 

function CalcDday(finalDay) { //디데이 계산기

    // 오늘 날짜+시간
    const today = new Date();

    const milliSecond = finalDay - today;
    const day = Math.floor(milliSecond / 1000 / 60 / 60 / 24);
    if (day === 0){
        return "D-day"
    }
    else{
        return "D-" + day;
    }
        
}

document.getElementById("dday1_dday").innerHTML = CalcDday(sub1_finalDay); //첫째칸 d-day 출력
document.getElementById("dday2_dday").innerHTML = CalcDday(sub2_finalDay); //둘째칸 d-day 출력
document.getElementById("dday3_dday").innerHTML = CalcDday(sub3_finalDay); //셋째칸 d-day 출력