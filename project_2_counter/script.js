let inc = document.getElementById("inc");
let res = document.getElementById("reset");
let dec = document.getElementById("dec");
let nm = document.getElementById("num");

let num = 0;

inc.addEventListener("click", increase);
res.addEventListener("click", reset);
dec.addEventListener("click", decrease);

function increase(){
    num++;
    nm.textContent = num;
    color();
}

function reset(){
    num = 0;
    nm.textContent = 0;
    color();
}

function decrease(){
    num--;
    nm.textContent = num
    color();
}

function color(){
    if(num<0){nm.style.color = "red";}
    else if(num==0){nm.style.color = "black";}
    else{nm.style.color = "green";}
}