#!/usr/bin/node
const args = process.argv;
function factorial (n) {
  if (!n || !parseInt(n)) {
    return 1;
  } else {
    const num = parseInt(n);
    if (num === 1) {
      return 1;
    }
    return num * factorial(num - 1);
  }
}
console.log(factorial(args[2]));
