var fs = require("fs");
fs.readFile('Input1.txt', function (err, data) {
if (err) {
return console.error(err);
}
console.log("Asynchronous read: " + data.toString());
});

var http = require ('http');
var fs = require ('fs');
http.createServer(function (req, res){
console.log("File is open at localhost:5000");
fs.readFile('Input1.txt', function(err, data){
res.write(data);
return res.end();
});
}).listen(5000);

// var fs = require('fs');
// fs.appendFile('Input1.txt','Adding New Content Using appendFile Method!',
// function (err){
// if(err)throw err;
// console.log('Saved!!!!');
// });

// var fs = require('fs');
// fs.open('Input2.txt','w',function(err,file){
// fs.writeFile('Input2.txt','I am added while open',function (err)
// {
// console.log('Content added and Saved!!');
// });
// if(err)throw err;
// console.log('Saved!');
// });

// var fs = require('fs');
// fs.writeFile('Input3.txt','',
// function (err){
// if(err)throw err;
// console.log('Content added and Saved!!');
// });

// var fs = require('fs');
// fs.unlink('Input3.txt',function (err){
// if(err)throw err;
// console.log('File Deleted!');
// });

// var fs = require('fs');
// fs.copyFile('Inputnew.txt','Input1.txt',
// function (err){
// if(err)throw err;
// console.log('File Copied!');
// });

// var fs = require('fs');
// fs.chmod('Input1.txt',
// function (err){
// if(err)throw err;
// console.log('File Truncated!');
// });

// const data = {
// name: "John Doe",
// age: 32,
// title: "Vice President of JavaScript"
// }
// const jsonStr = JSON.stringify(data);
// console.log(jsonStr);


// const buf1 = new Buffer.from('61326232633264');
// const buf2 = new Buffer.from('54686973206973204e6f64652e6a7320636c617373','hex');
// console.log(buf1.from('ascii'));
// console.log(buf1.toString());

// buf=new Buffer.alloc(50);
// n=buf.write('This is Node.js class');
// console.log('The number of octets are: '+ n);


// var buffer1 = Buffer.from('ABCD');
// var buffer2 = Buffer.from('abcd');
// var result = buffer1.compare(buffer2);
// if(result===0)
// {console.log(buffer1 +"is equal To " + buffer2);
// }
// else
// {
// console.log(buffer1 +" is not equal to " +buffer2);
// }