def topDown(prices):
    memo = {}
    def dfs(i, money):
        if i == len(prices) - 1:
            return 0

        if (i, money) in prices:
            return prices[(i, money)]
        
        buy = 1 + dfs(i + 1, money - prices[i] + 1) if money >= prices[i] and prices[i] != 0 else 0
        dontBuy = 0 + dfs(i + 1, money + 1)
        
        memo[(i, money)] = max(buy, dontBuy)
        return memo[(i, money)]
    
    return dfs(0, 1)

def bottomUp(prices):
    n = len(prices)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for money in range(1, n):
            buy = 1 + dp[i + 1][money - prices[i] + 1] if money >= prices[i] and prices[i] != 0 else 0
            dontBuy = 0 + dp[i + 1][money + 1]
            dp[i][money] = max(buy, dontBuy)

    return dp[0][1]

'''
Complexité: Boucle imbriquée sur n => O(n^2)
'''

x = [0,0,0,4,2,3,0,0,0,2]
y = topDown(x)
yy = bottomUp(x)
print(yy)