class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Track the minimum price
        max_profit = 0  # Initialize the maximum profit

        for price in prices:
            # Update the minimum price so far
            min_price = min(min_price, price)
            # Calculate the profit and update the maximum profit
            max_profit = max(max_profit, price - min_price)

        return max_profit


        