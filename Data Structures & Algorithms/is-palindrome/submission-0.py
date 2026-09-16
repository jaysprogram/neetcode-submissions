class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        r = len(s) - 1
        print(s)
        while l < len(s) and r > 0:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
        
        return True