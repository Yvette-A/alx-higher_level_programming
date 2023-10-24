#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const apiUrl = `http://swapi.co/api/films/${filmId}`;

request(apiUrl, function (error, response, body) {
	if (error) {
		console.log(error);
	} else {
		console.log(JSON.parse(body).title);
	}
});

