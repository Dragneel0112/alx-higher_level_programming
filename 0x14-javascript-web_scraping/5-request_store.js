#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = fs.createWriteStream(process.argv[3], 'utf-8');

request
  .get(url)
  .on('error', err => {
    console.log(err);
  })
  .pipe(file);
