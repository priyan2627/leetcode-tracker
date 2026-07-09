# Last updated: 7/9/2026, 10:21:01 AM
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        total = sum(nums)

        for i in range(len(nums) - 1, 1, -1):
            if total - nums[i] > nums[i]:
                return total
            total -= nums[i]

        return -1