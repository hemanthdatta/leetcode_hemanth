class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=dict.fromkeys(nums)
        return list(a)!=nums
        