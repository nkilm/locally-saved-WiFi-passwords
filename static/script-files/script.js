console.log("linked!");


const keys = document.querySelectorAll(".key")


keys.forEach((key)=>{
    if(key.textContent==="--None--"){
        const parent = key.parentNode;
        parent.style.color = "#db7070";
    }
})








