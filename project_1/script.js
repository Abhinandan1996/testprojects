let btn = document.getElementById("btn");
let bg = document.getElementById("bg");
let num;
let edit = document.getElementById("cname");
let str;
changebg();

btn.addEventListener("click", changebg);
function changebg(){
    str = "#";
    let i;
    for(i = 0; i < 6; i++){
        let sam = "0123456789abcdef";
        num = Math.random() * 16;
        num = Math.floor(num);
        str = str + sam[num];
        edit.textContent = str;
        
    }
    bg.style.backgroundColor =str;
    console.log(str);
}
