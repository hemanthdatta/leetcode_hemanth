from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # tails array
        for num in nums:
            # Find position to insert/replace
            idx = bisect_left(sub, num)
            if idx == len(sub):
                sub.append(num)      # extend LIS
            else:
                sub[idx] = num       # replace to keep tail minimal
        return len(sub)
