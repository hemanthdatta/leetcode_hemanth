from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        curr_sum = 0
        max_sum = 0
        
        left = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            count[nums[right]] += 1
            
            # If window is larger than k, shrink from left
            if right - left + 1 > k:
                count[nums[left]] -= 1
                curr_sum -= nums[left]
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            
            # If window size is exactly k and all elements are distinct
            if right - left + 1 == k and len(count) == k:
                max_sum = max(max_sum, curr_sum)
        
        return max_sum
