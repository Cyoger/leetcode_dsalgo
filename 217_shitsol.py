class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        
        l = 0
        r = l+1
        
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            else:
                l+=1
                r+=1

        return False
                

if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([0]))
    