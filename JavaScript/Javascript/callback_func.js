const greet = ()=>{
    console.log("Hello World")
}

setTimeout(greet, 1000)

const a = function(){
    console.log("I am a")
}

const b = function(c){
    c()
}

b(a)