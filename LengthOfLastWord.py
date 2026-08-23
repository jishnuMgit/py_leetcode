class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=s.rstrip()
        x=s.split()
        return len(x[-1])
        




word = "   fly me   to   the moon  "

solution=Solution()

print(solution.lengthOfLastWord(word))