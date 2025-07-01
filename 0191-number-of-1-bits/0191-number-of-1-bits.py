class Solution:
    def hammingWeight(self, n: int) -> int:
        a=0
        while(n):
            n&=(n-1)
            a+=1
        return a
        