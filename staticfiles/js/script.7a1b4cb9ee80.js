const create_todo_btn = document.getElementById("create-todo");
const is_authenticated = document.getElementById("is_authenticated");
const get_started_btn = document.getElementById("get-started");

create_todo_btn.addEventListener("click", function() {
    create_todo_btn.style.backgroundImage = "none";
    create_todo_btn.style.backgroundColor = "rgb(224, 224, 224)";
    create_todo_btn.style.borderColor = "#5aff3d";
})

get_started_btn.addEventListener("click", function() {
    if (is_authenticated.innerHTML == "True") {
        get_started_btn.style.backgroundImage = "none";
        get_started_btn.style.backgroundColor = "rgb(224, 224, 224)";
        get_started_btn.style.borderColor = "#5aff3d";
    } else {
        get_started_btn.style.backgroundImage = "none";
        get_started_btn.style.backgroundColor = "rgb(224, 224, 224)";
        get_started_btn.style.borderColor = "#ff0000";
    }
})

var i = 0;
var txt = 'Start Planning'; /* The text */
var speed = 50; /* The speed/duration of the effect in milliseconds */

document.getElementById('id_title_search').innerHTML = "Search for"

function typeWriter() {
    if (i < txt.length) {
        document.getElementById("plan").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}