def twosum(self, nums, target):
    s = len(nums)
    
    for i in range(s):
        for j in range(i+1, s):
            if nums[i] + nums[j] == target:
                return [i, j]
            
    return []