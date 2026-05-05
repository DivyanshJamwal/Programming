const prompt = require("prompt-sync")()

let age = prompt("Enter the age: ", 18)

console.log("Age requirement for license is 18 years")
console.log("Your age is: ",age)


//Conditional Statement

// if(age >= 18){
//     if(age < 50){
//         console.log("You are eligible for license")
//     }
//     else{
//         console.log("You need to renew your license")
//     }
// }
// else{
//     console.log("You are not eligible for license")
// }

// inline ternary operator 

age>=18 ? ((age<50) ? console.log("You are eligible for license") : console.log("You need to renew your license")) : console.log("You are not eligible for license")

