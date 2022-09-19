#! INCOMPLETE: DOESNT WORK. NO CLUE WHAT THE PROBLEM WANTS

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c=0
        for i in range(len(nums)-1):
            if(nums[i] == val): 
                nums.pop(i)
                c+=1
        for i in range(c):
            nums.append("_")
        return nums
        
s = Solution()

print(s.removeElement([3,2,2,3], 3))
