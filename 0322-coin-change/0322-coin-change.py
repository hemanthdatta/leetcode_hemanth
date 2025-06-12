from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def solve(cv, amount):
            if amount == 0:
                return 0
            if cv < 0:
                return -1
            if (cv, amount) in dp:
                return dp[(cv, amount)]

            res = float('inf')

            # Option 1: take current coin if possible
            if coins[cv] <= amount:
                take = solve(cv, amount - coins[cv])
                if take != -1:
                    res = min(res, 1 + take)

            # Option 2: skip current coin
            skip = solve(cv - 1, amount)
            if skip != -1:
                res = min(res, skip)

            # Finalize result
            dp[(cv, amount)] = -1 if res == float('inf') else res
            return dp[(cv, amount)]

        return solve(len(coins) - 1, amount)
