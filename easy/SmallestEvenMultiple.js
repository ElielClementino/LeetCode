// https://leetcode.com/problems/smallest-even-multiple/description/

let smallest = 0
let n = 5

var smallestEvenMultiple = function(n) {
    if (n % 2 == 0) {
        return n
    }
    return n * 2
};
smallest = smallestEvenMultiple(n)
console.log(smallest)