class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {i: s.count(i) for i in set(s)}
        t_dict = {i: t.count(i) for i in set(t)}
        if s_dict == t_dict:
            return True
        else:
            return False
        
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram("abcd", "cabd"))
        
        
        
