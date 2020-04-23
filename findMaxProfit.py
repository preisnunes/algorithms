#Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#Note that you cannot sell a stock before you buy one.
def maxProfit(prices: list) -> int:
    if len(prices) == 0:
        return 0
    dp = [0]
    price_min = prices[0]
    
    for i in range(1, len(prices)):
        dp.append(max(dp[i-1], prices[i]-price_min))
        if prices[i] < price_min:
            price_min = prices[i]
            
    return dp[-1]

print(maxProfit([7,1,5,3,6,4]))