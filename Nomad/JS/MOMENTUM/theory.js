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
console.log(daysOfWeek[1]);

// Add one mor day to the Array
daysOfWeek.push("sun")