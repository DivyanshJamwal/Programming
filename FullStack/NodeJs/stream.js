const fs = require('fs');
const http = require('http');
const readStream = fs.createReadStream('Input1.txt');
const writeStream = fs.createWriteStream('output.txt');
readStream.pipe(writeStream);
http.createServer((req, res) => {
const fileStream = fs.createReadStream('Input1.txt');
fileStream.on('open', () => {
res.writeHead(200, { 'Content-Type': 'text/plain' });
fileStream.pipe(res);
});
fileStream.on('error', (err) => {
res.writeHead(404, { 'Content-Type': 'text/plain' });
res.end('File not found');
});
}).listen(3000, () => {
console.log('Server is running on port 3000');
});

http.createServer((req, res) => {
const writeStream = fs.createWriteStream('requestData.txt');
req.on('data', (chunk) => {
writeStream.write(chunk);
});
req.on('end', () => {
writeStream.end();
res.end('Data received and saved');
});
}).listen(3001, () => {
console.log('Server is running on port 3001');
});