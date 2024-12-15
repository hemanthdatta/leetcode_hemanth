class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[0,0]
        n=len(nums)
        for i in range(n):
            for j in range(n-1):
                if nums[i]+nums[j] == target:
                    l[0],l[1]=i,j
                    break
        return l
            

        