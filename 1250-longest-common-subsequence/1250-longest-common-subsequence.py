class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp={}
        m,n=len(text1),len(text2)
        def solve(m,n):
            if m==0 or n==0:
                return 0
            elif (m,n) in dp:
                return dp[(m,n)]
            else:
                if text1[m-1]==text2[n-1]:
                    c=1+solve(m-1,n-1)
                else:
                    c1=solve(m-1,n)
                    c2=solve(m,n-1)
                    c=max(c1,c2)
                dp[(m,n)]=c
            return dp[(m,n)]
        return solve(m,n)