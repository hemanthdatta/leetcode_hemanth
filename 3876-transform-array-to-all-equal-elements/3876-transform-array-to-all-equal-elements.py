class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        c1=0
        c2=0
        #+1
        if n<2:
            return True
        nums2=nums.copy()
        for i in range(n-1):
            if nums[i]==-1:
                nums[i]=1
                nums[i+1]*=-1
                c1+=1
        for i in range(n-1):
            if nums2[i]==1:
                nums2[i]=-1
                nums2[i+1]*=-1
                c2+=1

        if nums[-1]==nums[-2]:
            if c1<=k:
                return True
        if nums2[-1]==nums2[-2]:
            if c2<=k:
                return True
        return False



              
        


            


        

        