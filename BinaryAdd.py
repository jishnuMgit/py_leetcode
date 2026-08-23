class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i=len(a) - 1
        j=len(b) - 1
        carry=0
        result=[]
        while i >=0 or j >=0 or carry:
            digit_A=int(a[i]) if i>=0 else 0 
            digit_B = int(b[j]) if j>=0 else 0 
            total = digit_A + digit_B + carry
            result.append(str(total%2))
            carry = total // 2
            i =i - 1
            j =j - 1

        return ''.join(result[::-1])
solution=Solution()

print(solution.addBinary("11","1"))         

         
     

        