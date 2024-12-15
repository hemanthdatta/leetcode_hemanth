class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result,counter=0,0
        for x in nums:
            if x==1:
                counter=counter+1
            else:
                counter=0
            result=max(counter,result)

        return result
        