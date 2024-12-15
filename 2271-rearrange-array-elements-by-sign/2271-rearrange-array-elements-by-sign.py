class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1=[]
        l2=[]
        for num in nums:
            if num>0:
                l1.append(num)
            else:
                l2.append(num)
        for i in range(0,len(nums),2):
            nums[i]=l1[i//2]
        for i in range(1,len(nums),2):
            nums[i]=l2[i//2]
        return nums

        