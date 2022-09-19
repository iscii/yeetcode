/* 
    10/10/2021
    Runtime: 76 ms
    Memory Usage: 40.6 MB
*/

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
 var strStr = function(haystack, needle) {
    if(!haystack.includes(needle)) return -1
    for(i=0;i<=haystack.length-needle.length;i++){
        if(haystack.substr(i,needle.length) == needle){
            return i
        }
    }
};