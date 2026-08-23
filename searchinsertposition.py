# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
#  return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
class Solution(object):
    def searchInsert(self, nums, target):
        for index, x in enumerate(nums):
            if x >= target:
                return index

        return len(nums)
        


nums = [0,3,5,6]
target = 5

solution=Solution()
print(solution.searchInsert(nums,target))