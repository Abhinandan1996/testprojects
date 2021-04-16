let nav = document.getElementById("navigation-dropdown");
let btn = document.getElementById("bgbtn");
btn.addEventListener("click", toggle);
function toggle(){
    nav.classList.toggle("hide");
}