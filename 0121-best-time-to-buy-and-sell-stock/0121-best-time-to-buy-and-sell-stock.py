class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        l,r=0,1
        n=len(prices)
        while r<n:
            if prices[l]<prices[r]:
                pf=prices[r]-prices[l]
                maxi=max(maxi,pf)
            else:
                l=r
            r+=1
        return maxi


        