function maxDifference(numbers) {
    let max = Math.max(numbers);
    let min = Math.min(numbers);
    return max - min;
}

console.log(maxDifference(3, 10, 5, 8));