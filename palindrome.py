result = ""
text = "A man, a plan, a canal: Panama"
for char in text:
    if char.isalnum():
        result += char 

text1=list(result)

result= result.lower()
l1=len(text1)
arr1=[]
for i in range(len(text1)):
    arr1.append(text1[l1-1-i])

text = ''.join(arr1)
text=text.lower()

print(result)
print(text)

if result ==text :
    print(True)
else:
    print(False)    


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result=""
        for char in s:
          if char.isalnum():
             result += char 

        text1=list(result)
        
        result= result.lower()
        l1=len(text1)
        arr1=[]
        for i in range(len(text1)):
            arr1.append(text1[l1-1-i])
        
        text = ''.join(arr1)
        text=text.lower()
        
        print(result)
        print(text)
        
        if result ==text :
            return True
        else:
            return False  

        
        
        