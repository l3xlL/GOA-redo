const user = {
  name: "barbare",

  greet() {
    console.log(`hey ${this.name}, how are you`);
  }
};

user.greet();