var express= require('express');
var app = express()

var mylogger = function(req,res,next){
    console.log('Logged')
    next()
}
app.use(mylogger)
app.get('/',function(req,res){
    res.send('Hello World')
})
app.listen(2000);