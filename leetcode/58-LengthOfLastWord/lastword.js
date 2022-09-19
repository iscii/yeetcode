/* 
    9/19/2022
    Runtime: 94 ms
    Memory Usage: 42.1 MB
*/

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    //split string into array by " "
    //take last one, return its length
        //may be too easy cos built in js
        
    //instead, loop from back of string till a letter, collect the index of that letter, then until a space, and collect the index of that space 
    start = end = 0;
    flag = false;
    
    for(i=s.length;i>0;i--){
        if(!flag && s.substring(i-1, i) !== " "){
            end = i;
            flag = true;
        }
        if(flag && s.substring(i-1, i) == " "){
            start = i;
            break;
        }
    }
    return end-start;
};

console.log(lengthOfLastWord("Hello World"));
console.log(lengthOfLastWord("   fly me   to   the moon  "));
console.log(lengthOfLastWord("luffy is still joyboy"));