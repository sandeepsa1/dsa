def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count if amount == 0 else -1

coins = [1, 5, 10, 25]
amount = 95
print(min_coins(coins, amount))