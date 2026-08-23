class Solution(object):
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            num = target - nums[x]

            if num in nums:
                i = nums.index(num)

                if i != x:
                    return [i, x]
        

nums = [3,3]
target = 6

solution = Solution()
print(solution.twoSum(nums, target))


    



                     



 