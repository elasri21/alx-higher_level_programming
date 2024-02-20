#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const movies = JSON.parse(body).results;
    const charMovies = movies.filter(
      c => c.characters.find(i => i.match(/\/people\/18\/?$/))
    );
    console.log(charMovies.length);
  }
});
