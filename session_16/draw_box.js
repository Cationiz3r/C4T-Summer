function changeColor() {
    document.getElementById("rect").style.fill = "#FF0000"
}

var visibility = true
function changeVisibility() {
    if (visibility) {
        document.getElementById("target").style.display = "none"
        visibility = false
    } else {
        document.getElementById("target").style.display = "block"
        visibility = true
    }
}