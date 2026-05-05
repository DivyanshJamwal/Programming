const express = require("express")
const app = express()
const PORT = 4000

var data = []

app.use(express.json())

app.get("/todos",(req,res)=>{
    res.status(200).json(data)
})

app.post("/todos/new",(req,res)=>{
    const {title, priority} = req.body
    const newTask = {
        title : title,
        priority : priority,
        id : generateUniqueId(),
        status : "pending"
    }
    data.push(newTask)
    res.status(201).json({
        success : true,
        id : newTask.id
    })
})

app.put("/todos/update",(req,res)=>{
    const { id,title, priority,status } = req.body;

    const taskIndex = data.findIndex(task=>task.id===id)

    const oldTask = data[taskIndex]

    const newTask = {
        ...oldTask,
    }
    if(title){
        newTask.title = title
    }
    if(priority){
        newTask.priority = priority
    }
    if(status){
        newTask.status = status
    }

    data.splice(taskIndex, 1, newTask)

    res.writeHead(200, {"Content-Type" : "application/json"})
    res.end(JSON.stringify({
    success : true
}))
})
app.listen(PORT,()=>{
    console.log("Express Server running on port",PORT)
})

function generateUniqueId() {
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    let uniqueId = "";
    for (let i = 0; i < 6; i++) {
      uniqueId += characters.charAt(
        Math.floor(Math.random() * characters.length)
      );
    }
    return uniqueId;
}


// fs.watch("data/students.txt", (eventType, fileName)=>{
//     console.log(fileName, " is changed")
//     console.log(eventType)
// })

// server.get('/testing', async (req, res)=>{
   
//     try{

//         // TODO 1 : Create a folder/directory
//         // fs.mkdirSync("data")

//         // fs.mkdir('images/birthday/cake_cutting', {recursive : true}, (err)=>{
//         //     if(err){
//         //         throw new Error("Error while creating folder")
//         //     }
//         //     console.log("folder created successfully")
//         //     res.send({
//         //         success : true
//         //     })    
//         // })

//         // TODO 2 : Create a file

//         // await fs.writeFileSync("data/students.txt", "Dipesh Raj", 'utf-8')

//         // fs.writeFile("data/projects.txt", "tripkaro.in", 'utf-8', (err)=>{
//         //     if(err){
//         //         throw new Error("Error while creating file")
//         //     }
//         //     res.send({
//         //         success : true
//         //     })
//         // })

//         // TODO 3 : Update a file

//         // fs.appendFileSync("data/students.txt", "\nDivyansh Kumar", "utf-8")

//         // await fs.appendFileSync("data/topics.txt", "React\n", "utf-8")

//         // TODO 4 : Read a file

//         // const result = await fs.readFileSync("data/students.txt", "utf-8")

//         // console.log(result)

//         // TODO 5 : Read a directory

//         // const files = fs.readdirSync("data")

//         // console.log(files)

//         // files.forEach((name)=>{
//         //     const result = fs.readFileSync(`data/${name}`, "utf-8")
//         //     console.log(result)     
//         // })

//         // TODO 6 : To check the existence of a file or folder

//         // if(fs.existsSync("data/projects.txt")){
           

//         //     // TODO 7 : Delete a file

//         //     fs.unlinkSync("data/projects.txt")

//         // }

//         // TODO 8 : Rename File or Folder

//         // fs.renameSync("uploads", "old_uploads")

//         fs.renameSync("data/topics.txt", "data/frontend_topics.txt")

//         res.send({
//             success : true
//         })  

//     }catch(err){
//         console.log(err)
//         res.send({
//             success : false
//         })
//     }

// })