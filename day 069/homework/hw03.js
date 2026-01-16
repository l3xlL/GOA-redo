const counter = {
  count: 0,

  increment() {
    this.count++;
    return this;
  },
  decrement() {
    this.count--;
    return this;
  },
  show() {
    console.log(this.count);
    return this;
  }
};

counter.increment().increment().decrement().show();