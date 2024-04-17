const express = require('express')
const app = express()
app.use(function(req, res, next) {
console.log('hello world')
next() })
app.use(function(req, res, next) {
console.log('happy holidays')
next() })
app.get('/', function (req, res) {
res.send('Home page') })
app.get('/hello', function (req, res) {
res.send('Hello page') })
app.get('/welcome', function (req, res) {
res.send('welcome Page') })
app.get('/welcome/inside', function (req, res) {
res.send('you are in inside page') })
app.listen(3000)