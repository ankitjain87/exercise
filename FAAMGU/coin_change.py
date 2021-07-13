coins = [2]
amount = 3

def coin_change(coins, amount):
    if amount == 0:
        return 0

    dp = [float('inf')]*(amount+1)
    dp[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if i-coin >= 0:
                dp[i] = min(dp[i], dp[i-coin]+1)

    return dp[amount] if dp[amount] != float('inf') else -1


print(coin_change(coins, amount))

