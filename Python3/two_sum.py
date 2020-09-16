# Uses a hashmap!

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i in range(len(nums)):
            new_dict.update({nums[i]: i})
        for i in range(len(nums)):
            if (target - nums[i]) in new_dict:
                if new_dict.get(target - nums[i]) != i:
                    return [i, new_dict.get(target - nums[i])]
