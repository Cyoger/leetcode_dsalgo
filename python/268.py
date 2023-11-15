def missingNumber(nums):
    nums.sort()
    n = nums[-1]
    k = 0
    
    for i in range(len(nums)):
        if i != nums[i]:
            k = i

missingNumber([0,1])