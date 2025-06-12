class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        has=[0]*(len(nums)+1)
        has[0]=abs(nums[0]-nums[-1])
        for i in range(1,len(nums)):
            has[i]=abs(nums[i]-nums[i-1])
        return max(has)
        