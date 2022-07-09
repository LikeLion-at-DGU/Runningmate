var tasks = document.querySelectorAll(".chart-bars li");

var startDay
var endDay
tasks.forEach((task) => {
    var dataDuration = task.getAttribute("data-duration")
    var duration = dataDuration.split("-")
    if (duration[0] == "0") {
        startDay = "sun"
    } else if (duration[0] == "1") {
        startDay = "mon"
    } else if (duration[0] == "2") {
        startDay = "tue"
    } else if (duration[0] == "3") {
        startDay = "wed"
    } else if (duration[0] == "4") {
        startDay = "thu"
    } else if (duration[0] == "5") {
        startDay = "fri"
    } else if (duration[0] == "6") {
        startDay = "sat"
    }
    if (duration[1] == "0") {
        endDay = "sun"
    } else if (duration[1] == "1") {
        endDay = "mon"
    } else if (duration[1] == "2") {
        endDay = "tue"
    } else if (duration[1] == "3") {
        endDay = "wed"
    } else if (duration[1] == "4") {
        endDay = "thu"
    } else if (duration[1] == "5") {
        endDay = "fri"
    } else if (duration[1] == "6") {
        endDay = "sat"
    }
    task.setAttribute("data-duration", `${startDay}-${endDay}`)
})