#!/usr/bin/node
const num = process.argv;
if (!parseInt(num[2]) || !num[2]) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(num[2]); i++) {
    console.log('C is fun');
  }
}
