class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars=[]
        for char in s:
            if char.isalnum():
                chars.append(char.lower())
        charstr="".join(chars)

        revstr=charstr[::-1]  
        if charstr==revstr:
            return True
        else:
            return False