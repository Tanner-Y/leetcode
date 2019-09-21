# Not sure what was difficult about this one. I probably did it wrong.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        middle = len(nums) // 2
        if len(nums) % 2 == 0:
            return (nums[middle-1] + nums[middle])/2
        else:
            return float(nums[middle])
        
