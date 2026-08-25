class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        newnum1 = []
        newnum2 = []

        if len(nums1) != m:
            for i in range(m):
                newnum1.append(nums1[i])
        else:
            newnum1 = nums1

        if len(nums2) != n:
            for i in range(n):
                newnum2.append(nums2[i])
        else:
            newnum2 = nums2

        for i in range(n):
            newnum1.append(newnum2[i])

        for j in range(len(newnum1)):
            for i in range(len(newnum1) - 1):
                if newnum1[i] > newnum1[i + 1]:
                    temp = newnum1[i]
                    newnum1[i] = newnum1[i + 1]
                    newnum1[i + 1] = temp

            nums1[:] = newnum1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

solution=Solution()
print(solution.merge(nums1,m,nums2,n))