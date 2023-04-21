from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for i in nums:
            if i not in check:
                check.add(i)
            else:
                return True
        return False 


if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([1,2,4,6]))