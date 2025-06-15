class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp={}
        def solve(s1,s2,m,n):
            if m==0 or n ==0:
                return 0
            elif (m,n) in dp:
                return dp[(m,n)]
            else:
                if s1[m-1]==s2[n-1]:
                    c=1+solve(s1,s2,m-1,n-1)
                else:
                    c1=solve(s1,s2,m-1,n)
                    c2=solve(s1,s2,m,n-1)
                    c=max(c1,c2)
                dp[(m,n)]=c
            return dp[(m,n)]
        return solve(text1,text2,m,n)      