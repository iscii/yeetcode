/* 
    9/19/2022
    Runtime: 68 ms
    Memory Usage: 42.4 MB
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    //requirement: O(log n) -> binary search

    /* old tries
    end case: if final element is not =, how to know when?
    
    idx = (Math.floor(nums.length/2))
    prev = idx

    start idx at middle (idx)
    if element is =, return idx
    otherwise if element <, set idx = Math.floor(idx/2)
    otherwise (el >), set idx = Math.floor((nums.length-idx)/2)
    
    idx = Math.floor((idx-prev)/2)

    maybe start at prev = nums.length
                  idx = (prev-0)/2 
    */

    /*
     Let's try to understand how to get to the next target first:
        if <, we are at idx-0/2
            if <, we are at idx-0/2
                if >, we are at previdx - idx/2
        if >, we are at (nums.length - idx)/2
            if >, we are at (nums.length - idx)/2
                if <, we are at previdx + (idx - previdx)/2

    | | | | | | | |
    16 - 8 / 2 = 4; 8 + 4 = 12
        16 - 12 / 2 = 2; 12 + 2 = 14
        12 - 8 / 2 = 2; 12 - 2 = 14
        bruh maybe i can just do idx + or - floor of half of num.length/2i (progressive) wtffffff

    Now for when to know the program does not find
        maybe if it's not = element and floor of half of num.length/2i = 0!! 
        (once there's only one element left, the value is 1. after that element, the value is 0.5, floored to 0. omfg.)

    TIME TO IMPLEMENT 
    note, figuring this out took maybe 10~15 mins, including pathetic failure but that's totally welcome
    */

    cur = idx = Math.floor(nums.length/2)

    while(cur != 0){
        if(nums[idx] == target) return idx;
        cur = Math.floor(cur/2)
        if(nums[idx] < target){
            idx -= cur;
        }
        else{
            idx += cur;
        }
    }
    // not found
    for(idx=0;idx<nums.length;idx++){
        if(nums[idx]>=target){
            break;
        }
    }
    return idx;
};

console.log(searchInsert([1,3,5,6], 5))
console.log(searchInsert([1,3,5,6], 2))
console.log(searchInsert([1,3,5,6], 7))