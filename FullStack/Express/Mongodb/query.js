// var MongoClient = require('mongodb').MongoClient;
// var url = "mongodb://localhost:27017/";
// MongoClient.connect(url)
// .then(client=> {
// var dbo = client.db("Univ");
// var request = { course: "HTML" };
// dbo.collection("student_data").find(request).toArray()
// .then(data=> {
// console.log(data);
// db.close();
// })
// .catch(err => {
// console.error("An error occurred:", err);
// })
// .catch(err => {
// console.error("An error occurred:", err);
// })
// });


// //Find documents whose name starts with letter R, ^ is regular expression operator
// /*var MongoClient = require('mongodb').MongoClient;
// var url = "mongodb://localhost:27017/student";

// MongoClient.connect(url, { useUnifiedTopology: true }, function(err, db) {
// if (err) throw err;
// var dbo = db.db("student");
// var query = {name: /^R/ };
// dbo.collection("student_details").find(query).toArray(function(err, result) {
// if (err) throw err;
// console.log(result);
// db.close();
// });
// });*/

// var MongoClient = require('mongodb').MongoClient;
// var url = "mongodb://localhost:27017/";
// MongoClient.connect(url)
// .then(client=> {
// var dbo = client.db("Univ");
// var request = { course: "HTML" };
// dbo.collection("student_data").find(request).toArray()
// .then(data=> {
// console.log(data);
// db.close();
// })
// .catch(err => {
// console.error("An error occurred:", err);
// })
// });


var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://127.0.0.1:27017/";
MongoClient.connect(url)
.then(client => {
var dbo = client.db("Univ");
var request = { course: "Node js" };
dbo.collection("Student_data").find(request).toArray()
.then(data => {
console.log(data);
client.close();
})
.catch(err => {
console.error("An error occurred:", err);
});
})
.catch(err => {
console.error("An error occurred while connecting to MongoDB:", err);
});