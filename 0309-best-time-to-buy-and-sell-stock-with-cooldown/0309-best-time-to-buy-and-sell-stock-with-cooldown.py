class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        n=len(prices)
        def solve(i,buyable):
            if i>=n:
                return 0
            if (i,buyable) in dp:
                return dp[(i,buyable)]
            c2=solve(i+1,buyable)
            if buyable:
                c1=solve(i+1,False)-prices[i]
                c=max(c1,c2)
            else:
                c1=solve(i+2,True)+prices[i]
                c=max(c1,c2)
            dp[(i,buyable)]=c
            return dp[(i,buyable)]
        return solve(0,True)