class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        if n < 2 :
            return n

        for i in range(3, n + 1):
           val = a + b #3 5 8
           a = b   #2 #3  5
           b = val #3 5  8

        return b


    
solution=Solution()    
print(solution.climbStairs(1))   