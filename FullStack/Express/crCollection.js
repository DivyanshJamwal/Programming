Collection: var MongoClient = require('mongodb').MongoClient; 
var url = "mongodb://127.0.0.1:27017/company"; 
MongoClient.connect(url, { useUnifiedTopology: true }, function(err, db) { 
  if (err) throw err; 
  var dbo = db.db("company"); 
  dbo.createCollection("Student_data", function(err, res) { 
    if (err) throw err; 
    console.log("Collection created"); 
    db.close(); 
  }); 
});