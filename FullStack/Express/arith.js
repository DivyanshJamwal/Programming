var express = require('express');
var app = express();
app.get('/',(req,res)=>{
    res.sendFile(__dirname+"/"+"Arith.html");
})
app.get('/add',(req,res)=>{
    var response = parseInt(req.query.fn)+parseInt(req.query.sn)
    response = response.toString();
    res.send('The sum is:'+response);
})
app.get('/sub',(req,res)=>{
    var response = parseInt(req.query.fn)-parseInt(req.query.sn)
    response = response.toString();
    res.send('The sub is:'+response);
})
app.get('/mul',(req,res)=>{
    var response = parseInt(req.query.fn)*parseInt(req.query.sn)
    response = response.toString();
    res.send('The mul is:'+response);
})
app.get('/div',(req,res)=>{
    var response = parseInt(req.query.fn)/parseInt(req.query.sn)
    response = response.toString();
    res.send('The div is:'+response);
})
app.listen(2000);