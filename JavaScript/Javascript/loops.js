//for loop

a = 1;

for (let i = 0; i < 10; i++) {
    console.log(a+i);
}

// for in loop

obj = {
    name : "Rahul",
    role : "Developer",
    company : "AIbase"
}

for (const key in obj) {
    console.log(key)
}

// for of loop

for (const c of "Rahul") {
    console.log(c)
}

// while loop

let i = 1;
while (i<6) {
    console.log(i);
    i++
}

// do while loop

let x = 10;
do {
    console.log(x);
    x++
}
while (x<6)