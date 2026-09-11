class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit > 0 if profit < 0 move window 
        # dynamic size window problem
        left, right = 0, 0
        res = 0
        while (right < len(prices)):
            profit = prices[right] - prices[left]
            print(profit)
            #print("right here: ", right)
            # while window condition broken
            while profit < 0:
                #print("left here: ", left)
                left += 1
                profit = prices[right] - prices[left]
            res = max(res, profit)
            right += 1
        return res 