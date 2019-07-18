
function get_property() {
    console.log(document.getElementById("rect").attributes.getNamedItem("width").nodeValue)
    console.log(document.getElementById("rect").attributes.getNamedItem("height").nodeValue)
}

function log() {
    console.log(document.getElementById("rect").attributes.getNamedItem("width").nodeValue)
}