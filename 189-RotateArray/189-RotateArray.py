# Last updated: 7/9/2026, 10:21:32 AM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])