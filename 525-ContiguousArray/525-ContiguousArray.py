# Last updated: 7/9/2026, 10:21:17 AM
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_length = 0
        first_index = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in first_index:
                max_length = max(max_length, i - first_index[prefix_sum])
            else:
                first_index[prefix_sum] = i

        return max_length