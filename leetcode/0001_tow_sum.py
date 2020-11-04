from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        空间换时间
        """
        d = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in d:
                return [d[find], i]
            else:
                d[nums[i]] = i
        