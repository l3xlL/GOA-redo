function mergeAndFilter(min, ...arrays) {
    let merged = [];
    for (let arr of arrays) {
        merged = merged.concat(arr);
    }
    return merged.filter(num => num > min);
}




console.log(mergeAndFilter(5, [1, 6, 3], [7, 0, 8]));