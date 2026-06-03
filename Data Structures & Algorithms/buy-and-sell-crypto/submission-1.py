class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suffix = deque()
        maxi = 0
        for i in range(len(prices)-1, -1, -1):
            maxi = max(maxi, prices[i])
            suffix.appendleft(maxi)
        # print(suffix)
        result = 0
        for i,price in enumerate(prices):
            result = max(result, suffix[i]-prices[i])
        # print(result)
        return result