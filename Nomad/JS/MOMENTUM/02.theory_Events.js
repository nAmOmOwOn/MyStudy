const h1 = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
    h1.style.color = "blue";
}

function handleMouseEnter() {
    h1.innerText = "Mouse is here";
}

function handleMouseLeave() {
    h1.innerText = "Mouse is gone!";
}

function handleWindowResize() {
    document.body.style.backgroundColor = "tomato";
}

function handleWindowCopy() {
    alert("copier!");
}

function handleWindowOffline() {
    alert("SOS no WIFI");
}

function handleWindowOnline() {
    alert("ALL GOOOOOD");
}

h1.addEventListener("click", handleTitleClick);
// title.onclick = handleTitleClick; 위 코드와 같음
h1.addEventListener("mouseenter", handleMouseEnter); // 마우스 커서에 관한 이벤트
h1.addEventListener("mouseleave", handleMouseLeave);

window.addEventListener("resize",handleWindowResize); // 창 크기에 관한 이벤트
window.addEventListener("copy", handleWindowCopy); // Ctrl + c 에 관한 이벤트
window.addEventListener("offline", handleWindowOffline); // 인터넷 연결에 관한 이벤트
window.addEventListener("online", handleWindowOnline);


// const h1 = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
    const currentColor = h1.style.color;
    let newColor;
    if (currentColor === "blue") {
        newColor = "tomato"
    } else {
        newColor = "blue"
    }
    h1.style.color = newColor; // 화면에 있는 h1.style.color 을 바꾸는 함수
}

h1.addEventListener("click", handleTitleClick);