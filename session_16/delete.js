
function main() {
    var delete_buttons = document.getElementsByClassName("delete_button");
    for (var i=0; i<delete_buttons.length; ++i) {
        var delete_button = delete_buttons[i];
        delete_button.addEventListener("click", function(event) {
            console.log(event);
            event.target.parentNode.remove();
        });
        console.log(i);
    }
}

window.onload = main;