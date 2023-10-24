#!/usr/bin/node
const request = require('request');
let apiUrl = 'https://swapi-api.alx-tools.com/api/films/' +  process.argv[2];
request(apiUrl, function (error, response, body) {
	console.log(error || JSON.parse(body).title);
});

