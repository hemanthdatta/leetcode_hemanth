class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        longest=0
        for n in a:
            if n-1 not in a:
                length=1
                while n+length in a:
                    length += 1
                longest=max(longest,length)
        return longest


        