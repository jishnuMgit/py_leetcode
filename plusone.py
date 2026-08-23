class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x=0
        for i in digits:
            x = x * 10 + i
        x=x + 1    
        result =[int(i) for i in str(x)] 
        return result

solution=Solution()

print(solution.plusOne([9]))