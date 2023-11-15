import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.findall(r'[a-zA-Z0-9]', s))
        return s.lower() == s[::-1].lower()
    
    
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome("race car"))