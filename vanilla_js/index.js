// const time = document.getElementById("time");

const today=new Date();
console.log(today);
document.getElementById("time").innerHTML =new Date();
const loginForm = document.querySelector("#login-form");
const loginInput = loginForm.querySelector("login-form input");
const greeting = document.querySelector("#greeting")

const HIDDEN_CLASSNAME="hidden"
const USERNAME_KEY = "username";
const colors = [
    "#ef5777",
    "#575fcf",
    "#4bcffa",
    "#34e7e4",
    "#0be881",
    "#f53b57",
    "#3c40c6",
    "#0fbcf9",
    "#00d8d6",
    "#05c46b",
    "#ffc048",
    "#ffdd59",
    "#ff5e57",
    "#d2dae2",
    "#485460",
    "#ffa801",
    "#ffd32a",
    "#ff3f34"
  ];
  const button1 = document.getElementById("button1");
  const button2 = document.getElementById("button2");
  const body = document.querySelector("body");
  const word = document.querySelectorAll('.word')
  
  function clickBackColor() {
    const bodyColor1 = colors[Math.floor(Math.random() * colors.length)];
    const bodyColor2 = colors[Math.floor(Math.random() * colors.length)];
    body.style.backgroundImage = `linear-gradient(to right, ${bodyColor1} , ${bodyColor2})`;
    // const fontColor = colors[Math.floor(Math.random() * colors.length)];

    // word[0].style.color = fontColor;
    // word[1].style.color = fontColor;
  }

  function clickFontColor() {
    const fontColor = colors[Math.floor(Math.random() * colors.length)];

    word[0].style.color = fontColor;
    word[1].style.color = fontColor;
  }
  button1.addEventListener("click", clickBackColor);
  button2.addEventListener("click", clickFontColor);

//   function onLoginbtnClick(){
//     const username = loginInput.value;
//     if(username === ""){
//         alert("please write your name")
//     }else if(username.length>15){
//         alert("Your name is too long")
//     }
// }

function onLoginSubmit(event){
    event.preventDefault();
    loginForm.classList.add(HIDDEN_CLASSNAME);
    const username = loginInput.value;
    localStorage.setItem(USERNAME_KEY, username);
}

// loginButton.addEventListener("click", onLoginbtnClick);
function paintGreetigns(username){
    greeting.innerText = `Hello${username}`;
    greeting.classList.remove(HIDDEN_CLASSNAME)
}

const savedUsername = localStorage.getItem(USERNAME_KEY)
if(savedUsername===null){
    loginForm.classList.remove(HIDDEN_CLASSNAME)
    loginForm.addEventListener("submit", onLoginSubmit)
}else{
    paintGreetigns(savedUsername)
}