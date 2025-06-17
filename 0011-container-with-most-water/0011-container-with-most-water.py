class Solution:
    def maxArea(self, height: List[int]) -> int:
        #maxi=max(maxi,a)
        n=len(height)
        l,r=0,n-1
        maxi=0
        while l<r:
            area=(min(height[l],height[r])*(r-l))
            maxi=max(maxi,area)
            if height[l]<=height[r]:
                l=l+1
            else:
                r=r-1
        return maxi

        