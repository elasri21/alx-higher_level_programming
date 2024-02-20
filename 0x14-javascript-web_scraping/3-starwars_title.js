#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const endPoint = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(endPoint, (err, res, body) => {
  if (res.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(`${movie.title}`);
  } else {
    console.log(err);
  }
});
