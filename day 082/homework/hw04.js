const users = [
  { name: "nika", age: 17 },
  { name: "nuca", age: 19 },
  { name: "ana", age: 21 }
];

const adultNames = users
  .filter(user => user.age >= 18)
  .map(user => user.name);

console.log(adultNames);