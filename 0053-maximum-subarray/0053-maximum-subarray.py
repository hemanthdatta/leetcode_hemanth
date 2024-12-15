class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxi=-1000000
        for i in range(len(nums)):
            sum=sum+nums[i]
            maxi=max(sum,maxi)
            if sum<0:
                sum=0
        return maxi

        