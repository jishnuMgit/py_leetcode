class Solution(object):
    def findMedianSortedArrays(self, list1, list2):

        # Add list2 into list1
        for x in list2:
            list1.append(x)

        # Manual sorting
        for i in range(len(list1)):
            for j in range(i + 1, len(list1)):

                if list1[i] > list1[j]:
                    temp = list1[i]
                    list1[i] = list1[j]
                    list1[j] = temp

        n = len(list1)

        # Odd length
        if n % 2 == 1:
            return list1[n // 2]

        # Even length
        else:
            middle1 = list1[n // 2 - 1]
            middle2 = list1[n // 2]

            return (middle1 + middle2) / 2.0

nums1 = [1, 2]
nums2 = [3,4]

solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))