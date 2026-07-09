# Last updated: 7/9/2026, 10:20:56 AM
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)

        max_freq = max(freq.values())

        ans = 0
        for count in freq.values():
            if count == max_freq:
                ans += count

        return ans