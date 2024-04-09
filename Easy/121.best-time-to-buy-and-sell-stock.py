class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_day = prices[0]
        for sell_day in prices[1:]:
            if sell_day > buy_day:
                max_profit = max(max_profit, sell_day - buy_day)
            else:
                buy_day = sell_day

        return max_profit
