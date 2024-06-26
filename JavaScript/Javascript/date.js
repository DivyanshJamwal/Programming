console.log("Start")

setTimeout(()=>{
    console.log("setTimeout callback is called")
},2000)

const startTime = new Date().getTime()

const duration = 10 * 1000

while((new Date().getTime()-startTime) < duration){
    //wait
}

console.log("While is Completed")

console.log("end")