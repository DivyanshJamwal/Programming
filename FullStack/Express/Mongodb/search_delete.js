var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://127.0.0.1:27017/";
app.use(bodyParser.urlencoded({ extended: false }));
app.get('/', function (req, res) {
res.sendFile( __dirname + "/" + "delete.html" );
})
app.post('/search', (req, res)=>{
MongoClient.connect(url)
.then(db=>
{
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
.catch(err => {
console.error("An error occurred while connecting to MongoDB:", err);
});
})
});
app.post('/delete', (req, res)=>{
MongoClient.connect(url)
.then(db=>{
var dbo = db.db("Univ");
dbo.collection("Student_data").deleteMany(req.body)
.then(data=> {
console.log(data);
db.close();
res.send("Successfully deleted: " +data.deletedCount+" Documents <br/>")
})
.catch(err => {
console.error("An error occurred:", err);
})
})
.catch(err => {
console.error("An error occurred while connecting to MongoDB:", err);
});
})
app.listen(2000,()=>
{
console.log("The server is Running at http://localhost:2000/")
});