# Last updated: 7/9/2026, 10:21:21 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1