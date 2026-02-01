let numbers = [1, 2, 3, 4, 5];
let a = [];
let sum = 0;
for (let num of numbers) {
    sum += num;
    a.push(sum);
}
console.log(a);