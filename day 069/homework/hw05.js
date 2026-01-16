const temperature = {
  celsius: 0,

  toFahrenheit() {
    console.log((this.celsius * 9) / 5 + 32);
    return this;
  },
  toKelvin() {
    console.log(this.celsius + 273.15);
    return this;
  }
};

temperature.celsius = 25;
temperature.toFahrenheit().toKelvin();