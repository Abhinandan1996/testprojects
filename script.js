let btn = document.getElementById("btn");
let bg = document.getElementById("bg");
let num;
let str;
changebg();

btn.addEventListener("click", changebg);
function changebg(){
    num = Math.random()*1677216;
    num = Math.floor(num);
    str = num.toString(16);
    console.log(str);

    if(str.length < 6)str = "#" +"0"*(6-str.length)+ str;
    else str = "#" + str;
    console.log(str);
    bg.style.backgroundColor = str;
    document.getElementById("cname").textContent = str;
}