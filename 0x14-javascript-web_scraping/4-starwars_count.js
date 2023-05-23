#!/usr/bin/node
// Counts number of movies with Wedge Antilles
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const jsonBody = JSON.parse(body);
  let count = 0;
  for (const result of jsonBody.results) {
    for (const character of result.characters) {
      if (character.includes(18)) {
        count++;
      }
    }
  }
  console.log(count);
});
