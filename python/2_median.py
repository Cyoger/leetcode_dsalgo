from typing import List


class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		n = []
		n = nums1 + nums2
		print(n)
		n.sort()
		median = 0
		if len(n) % 2 != 0:
			median = n[len(n)//2]
		else:
			median = (n[len(n)//2] + n[len(n)//2 - 1])/2 
		
		return median
        
    
s = Solution()

nums1 = [1, 2, 3]
nums2 = [5, 6, 7]

n = nums1 + nums2
print(type(n))
median = s.findMedianSortedArrays(nums1, nums2)

print(median)