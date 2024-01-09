#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
const keys = Object.keys(dict);
keys.forEach(k => {
  if (newDict[dict[k]]) newDict[dict[k]].push(k);
  else newDict[dict[k]] = [k];
});
