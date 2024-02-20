#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    for (const character of characters) {
      request.get(character, (err2, res2, body2) => {
        if (err2) {
          console.log(err2);
        } else {
          const names = JSON.parse(body2);
          console.log(names.name);
        }
      });
    }
  }
});
