#!/usr/bin/node
if (!process.argv[2]) {
  console.log(0);
} else {
  const length = process.argv.length;
  const nums = [0, 0];
  for (let i = 2; i < length; i++) {
    const num = parseInt(process.argv[i]);
    if (num > nums[0]) {
      nums[1] = nums[0];
      nums[0] = num;
    } else if (num > nums[1] && num < nums[0]) {
      nums[1] = num;
    }
  }
  console.log(nums[1]);
}
