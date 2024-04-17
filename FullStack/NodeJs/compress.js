const zlib1 = require('zlib');
const input = 'Hello, world!';
zlib1.deflate(input, (err, buffer) => {
if (!err) {
console.log('Compressed data:', buffer.toString('base64'));
}
});

const zlib = require('zlib');
const compressedData = Buffer.from('eJzzSM3JyddRKM8vyklRBAAgXgSK','base64');
zlib.inflate(compressedData, (err, Buffer) => {
if (!err) {
console.log('Decompressed data:', Buffer.toString());
}
});