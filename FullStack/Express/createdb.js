var MongoClient = require('mongodb').MongoClient; 
var url = "mongodb://127.0.0.1:27017/company"; 
MongoClient.connect(url, { useUnifiedTopology: true }, function(err, db) { 
  if (err) throw err; 
  console.log("Database created!"); 
  db.close(); 
 });