
const keys = document.querySelectorAll(".key")

keys.forEach((key) => {
    if (key.textContent === "--None--") {
        const parent = key.parentNode;
        parent.style.color = "#db7070";
    }
})

const buttons = document.querySelectorAll(".btn-remove");
// console.log(buttons);

function sendInfo(method, URL) {
    const xhr = new XMLHttpRequest();
    xhr.open(method, URL);
    xhr.onload=()=>{
        console.log(`status: ${xhr.status} ${xhr.statusText}`);
    }
    xhr.send();
}


buttons.forEach((btn) => {
    btn.addEventListener("click", (e) => {
        const wifiName = e.target.parentNode.parentNode.parentNode.querySelector("td").textContent
        const yesOrNo = confirm(`Are you sure you wan to delete \"${wifiName}\" from your system`);
        if(yesOrNo){

            const wifiObj = {
                name : wifiName
            }
            sendInfo("POST",`/${JSON.stringify(wifiObj)}`)
        }
    })
})







