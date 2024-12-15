class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1=0
        sum2=0
        for i in range(0,len(nums)+1):
            sum1=sum1+i
        for x in nums:
            sum2=sum2+x
        return sum1-sum2

