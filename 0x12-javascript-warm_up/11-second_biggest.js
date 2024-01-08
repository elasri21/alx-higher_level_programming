#!/usr/bin/node
const args = process.argv;
const nums = [];
for (let i = 2; i < args.length; i++) {
  nums.push(parseInt(args[i]));
}
if (args.length > 3) {
  let max = nums[0];
  let sMax = nums[0];
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > max) {
      max = nums[i];
    }
  }
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > sMax && nums[i] < max) {
      sMax = nums[i];
    }
  }
  console.log(sMax);
} else {
  console.log(0);
}
