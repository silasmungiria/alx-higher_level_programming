#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

const writeStream = fs.createWriteStream(filePath);

request(url).pipe(writeStream);

writeStream.on('finish', () => {
  console.log('The file has been saved!');
});

writeStream.on('error', (err) => {
  console.error(err);
});
