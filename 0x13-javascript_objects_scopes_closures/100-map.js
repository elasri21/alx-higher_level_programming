#!/usr/bin/node
const list = require('./100-data').list;
newList = list.map((curr, index) => curr * index);
console.log(list);
console.log(newList);
