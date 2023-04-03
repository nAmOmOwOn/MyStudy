
alert("hi") // 알림창

const a = 5; // const = 변경불가
const b = 2;
let myName = "nico"; // let = 변경가능

console.log(a + b);
console.log(a * b);
console.log(a / b);
console.log("hello " + myName)

myName = "nicolas"

console.log("your name is " + myName)

const daysOfWeek = ["mon", "tue", "wed", "thu", "fri" , "sat"];

// Get Item from Array
console.log(daysOfWeek[1]); // tue

// Add one mor day to the Array
daysOfWeek.push("sun");

// Objects

const player = {
    name : "nico",
    points : 10,
    fat : true,

};

console.log(player); // 전체 다 출력
console.log(player.name); // nico
console.log(player["name"]); // 위 입력값과 동일
player.fat = false; // 변경 가능
player.lastname = "potato"; // 추가 가능

// 함수
function sayHello1(nameOfPoerson, age) {
    console.log("Hello my name is " + nameOfPoerson +"and I'm " + age);
}

const player = {
    name: "nico",
    sayHello2 : function (otherPersonsName) {
        console.log("hello " + otherPersonsName + " nice to meet you");
    }
};
console.log(player.name) // nico
player.sayHello2("lynn") // hello lynn nice to meet you
// arg를 여러개 보내도 문제는 되지 않음, 지정한 갯수 만큼만 받음.

// HTML autofocus
// autofocus는 <form> 태그와 같이 사용되는 속성입니다. 
// 키보드 커서가 자동으로 autofocus 속성이 삽입된 태그로 이동됩니다.
// 웹사이트나 앱에서 회원가입이나 로그인을 하다보면 
// 웹페이지에 접속하자 마자 입력창에 커서가 깜빡이는 것을 
// 볼 수 있는 것이 좋은 예가 될 수 있습니다.

// const title = document.querySelector("#hello")
// const title = document.getElementById("hello") 이 두개는 같은 것을 찾는 문장
