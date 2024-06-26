var express= require('express');
var app = express()

app.get('/',function(req,res){
    res.download('test.txt',function(err){
        if(err){
            res.send('File not found');
            console.log('File not found');
        }
        else{
            res.send('File downloaded successfully');
            console.log('File downloaded successfully');
        }
    });
});
app.listen(2000);