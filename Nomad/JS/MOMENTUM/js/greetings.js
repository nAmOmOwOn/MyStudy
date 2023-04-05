const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input"); // 위에 문장하고 같은걸 찾음
const greeting = document.querySelector("#greeting");

const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";

function onLoginSubmit(event) {
    event.preventDefault();
    loginForm.classList.add(HIDDEN_CLASSNAME);
    // greeting.innerText = "Hello " + username; 아래 문장과 같은 문장!
    localStorage.setItem(USERNAME_KEY, loginInput.value);
    paintGreetings();
}

function paintGreetings() {
    const username = localStorage.getItem(USERNAME_KEY);
    greeting.innerText = `Hello ${username}`;
    greeting.classList.remove(HIDDEN_CLASSNAME);
};


const savedUsername = localStorage.getItem(USERNAME_KEY);
console.log(savedUsername);

if (savedUsername === null) {
    loginForm.classList.remove(HIDDEN_CLASSNAME);
    loginForm.addEventListener("submit", onLoginSubmit);
} else {
    paintGreetings();
}

