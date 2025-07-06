class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if target-nums[i] in nums :
                index = nums.index(target-nums[i])
                if index != i:
                    res.append(i)
                    res.append(index)
                    break
        return res


