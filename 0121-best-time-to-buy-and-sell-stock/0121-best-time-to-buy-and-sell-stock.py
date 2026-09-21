class Solution(object):
    def maxProfit(self, prices):
        minprice = float('inf')
        profit = 0
        for i in prices:
            minprice = min(minprice , i)
            profit = max(profit, i - minprice)
        return profit
        