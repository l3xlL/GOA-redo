let nums = [10, 0, 15, 20, 0, 5];
let zeroCount = 0;
for (let num of nums) {
    if (num === 0) zeroCount++;
}
console.log(zeroCount);