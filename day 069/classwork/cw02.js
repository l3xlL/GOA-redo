const car = {
  brand: "BMW",
  speed: 0,

  drive() {
    this.speed += 50;
    console.log(`car is driving at ${this.speed} km/h`);
  },

  stop() {
    this.speed = 0;
    console.log("car stopped");
  }
};

car.drive();
car.drive();
car.stop();