let words = ["aca", "world", "radar", "hello"];
let palindromes = [];
for (let word of words) {
    let reversed = word.split("").reverse().join("");
    if (word === reversed) {
        palindromes.push(word);
    }
}
console.log(palindromes);