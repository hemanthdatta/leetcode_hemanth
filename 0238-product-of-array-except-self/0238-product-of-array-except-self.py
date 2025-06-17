from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Step 1: Calculate left products
        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= nums[i]
        
        # Step 2: Multiply with right products
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
        
        return res
