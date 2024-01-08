#!/usr/bin/node
const num = process.argv;
if (!parseInt(num[2]) || !num[2]) {
  console.log('Missing size');
} else {
  let row = '';
  for (let i = 0; i < parseInt(num[2]); i++) {
    row += 'X';
  }
  for (let j = 0; j < parseInt(num[2]); j++) {
    console.log(row);
  }
}
