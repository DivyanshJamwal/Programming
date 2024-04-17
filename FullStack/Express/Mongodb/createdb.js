const MongoClient = require('mongodb').MongoClient;
const url = "mongodb://127.0.0.1:27017/Univ";
MongoClient.connect(url)
.then(db => {
console.log("Database created!");
db.close();
})
.catch(err => {
throw err;
});