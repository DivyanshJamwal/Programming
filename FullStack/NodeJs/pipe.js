const zlib= require('zlib');
const gzip = zlib.createGzip();
const fs = require('fs');
const inp = fs.createReadStream('Input1.txt');
const out = fs.createWriteStream('New.txt.gz');
inp.pipe(gzip).pipe(out)
console.log('File compressed');