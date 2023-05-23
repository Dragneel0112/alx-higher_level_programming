#!/usr/bin/node
// Lists characters that appear in movie
const request = require('request');
const movie = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movie;

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const result = JSON.parse(body);
  for (const character of result.characters) {
    request(character, (err, r, body) => {
      if (err) { console.log(err); }
      const result = JSON.parse(body);
      console.log(result.name);
    });
  }
});
