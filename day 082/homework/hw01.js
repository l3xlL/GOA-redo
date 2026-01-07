function evenAndGreaterThanTen(arr) {
  return arr.filter(num => num % 2 === 0 && num > 10);
}

console.log(evenAndGreaterThanTen([4, 10, 12, 15, 20, 7]));