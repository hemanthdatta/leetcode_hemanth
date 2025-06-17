class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num]=1
        h=sorted(h,key=lambda x:h[x],reverse=True)
        a=list(h)
        return a[:k]
        

        