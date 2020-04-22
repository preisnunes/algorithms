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