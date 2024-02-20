#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (res.statusCode === 200) {
    let ct = 0;
    const movie = JSON.parse(body).results;
    for (let i = 0; i < movie.length; i++) {
      const chars = movie[i].characters;
      for (let j = 0; j < chars.length; j++) {
        if (chars[j] === 'https://swapi-api.alx-tools.com/api/people/18/' || chars[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
          ct++;
        }
      }
    }
    console.log(ct);
  } else {
    console.log(err);
  }
});
