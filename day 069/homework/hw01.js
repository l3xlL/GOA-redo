const calculator = {
  a: 2,
  b: 5,

  add() {
    return this.a + this.b;
  },
  subtract() {
    return this.a - this.b;
  },
  multiply() {
    return this.a * this.b;
  },
  divide() {
    return this.a / this.b;
  }
};

console.log(calculator.add());
console.log(calculator.subtract());
console.log(calculator.multiply());
console.log(calculator.divide());