from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        sum_map = defaultdict(int)
        sum_map[0] = 1  # To handle the case where prefix_sum == k
        count = 0

        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in sum_map:
                count += sum_map[prefix_sum - k]
            
            sum_map[prefix_sum] += 1

        return count
