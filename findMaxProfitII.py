#Say you have an array prices for which the ith element is the price of a given stock on day i.
#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
#You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
def maxProfit(prices: list) -> int:
    if len(prices) == 0:
        return 0
    dp = [0]
    price_min = prices[0]
    for i in range(1, len(prices)):
        dp.append(max(dp[i-1], dp[i-1] + prices[i] - prices[i-1]))
    return dp[-1]