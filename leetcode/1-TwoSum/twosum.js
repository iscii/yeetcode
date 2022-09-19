/* 
    10/8/2021
    Runtime: 184 ms
    Memory Usage: 39.8 MB
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(i=0;i<nums.length;i++)
        for(j=i+1;j<=nums.length;j++)
            if(nums[i]+nums[j]==target) return [i,j];
};