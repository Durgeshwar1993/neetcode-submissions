class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        

        mini_buy = prices[0]
        profit = 0
        for sell in prices:
            profit = max(profit,sell-mini_buy)
            mini_buy = min(mini_buy,sell)

        return profit

           
