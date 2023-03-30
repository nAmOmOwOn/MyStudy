const age = prompt("How old are you?");
const age2 = parseInt(prompt("How old are you?"));

console.log(typeof age, typeof parseInt(age)) // 숫자 입력하면 타입은 string, int 나옴
                                              // 글자 입력하면 글자 나오고 NaN(Not a Number) 이 나옴


console.log(isNaN(age2)) // age2 가 number 이면 false, 아니면 true 를 반환

if (isNaN(age2 || age < 0)) {
    console.log("Please write a real positive number"); // 문자 입력 or 음수 입력시 이 문구가 console 에 출력됨
}
else if (age2 < 18) {
    console.log("You are too young");
}
else if (age2 >= 18 && age <= 50) { // && = AND , || = OR
    console.log("You can drink");
}
else {
    console.log("You can't drink");
}



