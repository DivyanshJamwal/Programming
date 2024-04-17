var url = require('url');
var adr = 'http://localhost:8080/default.htm?year=2024&month=March';
var q = url.parse(adr, true);
console.log("Protocol:",q.protocol);
console.log("Hostname:",q.host);
console.log("Pathname:",q.pathname);
console.log("Search:",q.search);
var qdata = q.query;
console.log("Month:",qdata.month);