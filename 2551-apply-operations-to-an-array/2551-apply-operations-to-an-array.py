class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # First pass: apply doubling and set to zero
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums[i - 1] = 2 * nums[i - 1]
                nums[i] = 0
        
        # Second pass: move non-zero elements to the front and zeros to the end
        result = []
        for num in nums:
            if num != 0:
                result.append(num)
        
        # Add zeros to the end of the result list
        result.extend([0] * (len(nums) - len(result)))
        
        return result
