#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const res = process.argv[3];
request(url, (err, response, body) => {
  if (err == null) {
    fs.writeFileSync(res, body);
  }
});
