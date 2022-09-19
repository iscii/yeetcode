/* 
    10/10/2021
    Runtime: 335 ms
    Memory Usage: 49 MB
 */

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    return [...x.toString()].reverse().join("") == x.toString();
};