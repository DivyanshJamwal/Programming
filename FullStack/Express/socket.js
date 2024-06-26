var express = require('express');
var app = express();
var http = require('http').createServer(app);
var io = require('socket.io')(http);
app.get('/', function(req, res) {
//res.sendFile( __dirname + "/" + "index.html" );
res.send('Hello I am in Socket.io')
});
io.on('connection', function(socket) {
console.log('A user connected');
socket.on('disconnect', function () {
console.log('A user disconnected');
});
});
http.listen(2000, function() {
console.log('listening on localhost:2000');
});