var express = require('express');
//var router = express.Router();
var app = express();
var wiki = require('./wiki.js');
// ...
app.use(wiki);
app.listen(2000);