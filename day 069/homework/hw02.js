const calculatorWithSymbol = {
  number1: 0,
  number2: 0,
  userSymbol: "",

  calculate() {
    switch (this.userSymbol) {
      case "+":
        return this.number1 + this.number2;
      case "-":
        return this.number1 - this.number2;
      case "*":
        return this.number1 * this.number2;
      case "/":
        return this.number1 / this.number2;
      default:
        return "error";
    }
  }
};

calculatorWithSymbol.number1 = Number(prompt("chawere pirveli ricxi:"));
calculatorWithSymbol.number2 = Number(prompt("chawere meore ricxi:"));
calculatorWithSymbol.userSymbol = prompt("chawere simbolo (+, -, *, /):");

console.log(calculatorWithSymbol.calculate());