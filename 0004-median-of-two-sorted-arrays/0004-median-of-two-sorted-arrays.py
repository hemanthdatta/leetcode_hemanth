class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=nums1+nums2
        l.sort()
        n=len(l)
        if n%2==0:
            median=(l[n//2]+l[(n-2)//2])/2
        else:
            median=l[n//2]
        return median