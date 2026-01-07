const nums = [-2, 3, 4, -1, 5];

const product = nums.reduce((acc, num) => {
  if (num > 0) {
    return acc * num;
  }
  return acc;
}, 1);

console.log(product);