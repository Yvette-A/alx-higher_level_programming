#!/usr/bin/node
const files = require('files');
const x = files.readFileSync(process.argv[2], 'utf8');
const y = files.readFileSync(process.argv[3], 'utf8');
files.writeFileSync(process.argv[4], x + y);
