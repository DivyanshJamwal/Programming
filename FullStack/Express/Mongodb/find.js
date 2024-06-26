var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://127.0.0.1:27017/";
app.use(bodyParser.urlencoded({ extended: false }));
app.get('/', function (req, res) {  
  res.sendFile( __dirname + "/" + "find.html" );  
})  
app.post('/search', (req, res)=>{
  MongoClient.connect(url) 
  .then(db=>{
    var dbo = db.db("Univ");
  dbo.collection("Student_data").find(req.body).toArray()
  .then(data=> {
        console.log(data);
    db.close();
    res.json(data);
  })
  .catch(err => {
    console.error("An error occurred:", err);
  })
})
.catch(err => {
console.error("An error occurred while connecting to MongoDB:", err);
});
});
app.listen(2000);