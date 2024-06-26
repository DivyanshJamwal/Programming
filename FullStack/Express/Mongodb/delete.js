var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://127.0.0.1:27017/";
MongoClient.connect(url)
.then(db=> {
var dbo = db.db("Univ");
var myquery = { name: "Tej" };
//var myquery = { address: /^O/ };Delete all documents were the address starts with the letter "O"
dbo.collection("Student_data").deleteMany(myquery)
.then(data=>
{
console.log("There are "+ data.deletedCount+ " Documents Deleted");
db.close();
})
.catch(err => {
console.error("An error occurred:", err);
})
})
.catch(err => {
console.error("An error occurred while connecting to MongoDB:", err);
})