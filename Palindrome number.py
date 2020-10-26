class Solution:
    def isPalindrome(self, x: int):     
        a = str(x)
       
    
        
        strs = ""
        null = ""
        for i in str(x):
            strs += "".join(i)
        for i in a[::-1]:
            null += "".join(i)

        if strs == null and x > 0 or x==0:
            return True
        else:
            return False
