class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        dp = [0]*n
        i = 1
        prev = 0
        while i<n:
            if s[i] == s[prev]:
                dp[i] = prev+1
                prev+=1
                i+=1
            elif prev == 0:
                dp[i] = 0
                i+=1
            else:
                prev = dp[prev-1]
        print(dp)
        return s[:dp[-1]]