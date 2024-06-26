//Shallow Copy
const student = {name: "Rahul",
                age: 24,
                location: "Delhi"}

// let student1 = student
// student1.name = "Aditya"

//Deep Copy

// let student1 = JSON.stringify(student)
// student1 = JSON.parse(student1)

// student1.name = "Aditya"

// console.log(student, "student")
// console.log(student1, "student1")

//spread syntax
const student1 = {...student}
student1.age = 28

console.log(student, "student")
console.log(student1, "student1")
