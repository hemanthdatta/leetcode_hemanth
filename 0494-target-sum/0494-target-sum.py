class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #same as perfect sum, 
        s=sum(nums)
        n=len(nums)
        x=s+target
        if abs(target)>s:
            return 0
        if x%2!=0:
            return 0
        else:
            x=x//2
        dp=[[0]*(x+1) for i in range(n)]
        for i in range(len(nums)):
            for j in range(x+1):
                sm=j
                item=nums[i]
                if i==0:
                    if sm==0:
                        if item==0:
                            dp[i][j]=2
                        else:
                            dp[i][j]=1
                    elif item==sm:
                        dp[i][j]=1
                else:
                    if item<=sm:
                        dp[i][j]=dp[i-1][sm-item]+dp[i-1][sm]
                    else:
                        dp[i][j]=dp[i-1][sm]
        return dp[n-1][x]
                    
        