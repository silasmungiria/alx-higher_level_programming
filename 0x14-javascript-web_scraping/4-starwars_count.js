#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = 18;

request(url, function (err, response, body) {
  if (!err) {
    const { results } = JSON.parse(body);

    const count = results.reduce((count, films) => {
      const hasCharacterWithId18 = films.characters.find((character) => character.endsWith('/characterId/'));
      return hasCharacterWithId18 ? count + 1 : count;
    }, 0);

    console.log(count);
  }
});
