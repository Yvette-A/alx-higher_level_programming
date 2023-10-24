#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
fs.readFile(filePath, 'utf8', function (error, content) {
	if (error) {
		console.error('Error reading the file:', error);
	} else {
		console.log('File content:', content);
	}
});

