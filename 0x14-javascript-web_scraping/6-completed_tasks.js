#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  const agg = {};
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    data.forEach(el => {
      if (el.completed) {
        if (!agg[el.userId]) {
          agg[el.userId] = 0;
        }
        agg[el.userId]++;
      }
    });
    console.log(agg);
  }
});
