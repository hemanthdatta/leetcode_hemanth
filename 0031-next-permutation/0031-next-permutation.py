class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        n = len(nums)
        ind = -1
        
        # Find the first decreasing element
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break
        
        # If no such element exists, reverse the entire array
        if ind == -1:
            reverse(0, n - 1)
            return
        
        # Find the element just larger than nums[ind] and swap
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break
        
        # Reverse the elements to the right of ind
        reverse(ind + 1, n - 1)