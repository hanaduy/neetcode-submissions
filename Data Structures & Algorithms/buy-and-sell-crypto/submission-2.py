class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_price = prices[0]

        for price in prices:
            min_price = min(price, min_price)
            max_p = max(max_p, price-min_price)
            

        return max_p