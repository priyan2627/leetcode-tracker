# Last updated: 7/9/2026, 10:21:11 AM
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            result.extend([val] * freq)

        return result