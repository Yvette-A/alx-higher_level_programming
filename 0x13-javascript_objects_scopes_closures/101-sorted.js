#!/usr/bin/node
const dictionary = require('./101-data.js').dict;
const reversedDictionary = {};
for (const key in dictionary) {
  const value = dictionary[key];
  if (reversedDictionary[value] === undefined) {
    reversedDictionary[value] = [key];
  } else {
    reversedDictionary[value].push(key);
  }
}
console.log(reversedDictionary);
