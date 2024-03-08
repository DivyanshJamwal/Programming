var prompt = require('prompt-sync')();
var num1 = prompt("Enter first Number: ");
var num2 = prompt("Enter second Number: ");
num1 = parseInt(num1);
num2 = parseInt(num2);
if(isNaN(num1)||isNaN(num2)){
    console.log("Invalid Number")
}
else{
    console.log("Addition: ",num1+num2)
    console.log("Subtraction: ",num1-num2)
    console.log("Multiplication: ",num1*num2)
    console.log("Division: ",num1/num2)
}