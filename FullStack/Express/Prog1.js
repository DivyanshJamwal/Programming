const express = require('express');
const app = express();

// app.get('/', (req, res) => {
//   res.send('Hello, World!');
// });
app.get('/',(req,res)=>{
    res.sendFile(__dirname+"/"+"Prog1.html");
});

var bodyparser = require('body-parser');
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended:false}))

app.post('/submit',(req,res)=>{
    response={
        fname:req.body.fname,
        lname:req.body.lname,
        age:req.body.age
    }
    res.send("The result is: " + JSON.stringify(response))
})

// app.get('/submit',(req,res)=>{
//     response={
//         fname:req.query.fname,
//         lname:req.query.lname,
//         age:req.query.age
//     }
//     res.send("The result is: " + JSON.stringify(response))
// })

app.listen(2000);