class Solution(object):
    def maxProfit(self, prices):   
        max = 0
        result = 0
        for i in range(self.find_pro_day(prices), len(prices)):
            for j in range(i+1, len(prices)):
                result = prices[j] - prices[i]
                if result >= max:
                    max = result
        return max
    def find_pro_day(self,prices):
        for i in range(1, len(prices)):
            if prices[i-1]<prices[i]:
                return i - 1
        return -1