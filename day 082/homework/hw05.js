const prices = [100, 50, 25];

const total = prices
  .map(price => price * 0.8)
  .reduce((sum, price) => sum + price, 0);

console.log(total);