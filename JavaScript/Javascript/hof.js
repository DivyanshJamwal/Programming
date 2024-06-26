const a = ()=>{
    return ()=>{
        console.log("Hello")
    }
}

const temp = a()
console.log(temp)