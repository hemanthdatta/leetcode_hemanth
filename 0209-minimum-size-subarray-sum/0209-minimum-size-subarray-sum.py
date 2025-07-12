class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #shrinking window
        n=len(nums)
        l=0
        mini=float('inf')
        curr=0
        for r in range(n):
            curr=curr+nums[r]
            while curr>=target:
                mini=min(mini,r-l+1)
                curr-=nums[l]
                l+=1
        return 0 if mini==float('inf') else mini

        