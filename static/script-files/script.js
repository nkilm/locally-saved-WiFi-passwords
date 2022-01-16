console.log("linked!");


const keys = document.querySelectorAll(".key")


keys.forEach((key)=>{
    if(key.textContent==="--None--"){
        const parent = key.parentNode;
        parent.style.color = "#db7070";
    }
})

const buttons = document.querySelectorAll(".btn-remove");
// console.log(buttons);

buttons.forEach((btn)=>{
    btn.addEventListener("click",(e)=>{
        const wifiName = e.target.parentNode.parentNode.parentNode.querySelector("td").textContent
        console.log(wifiName)
    })
})







