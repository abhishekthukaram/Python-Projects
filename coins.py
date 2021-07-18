"""
You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
"""

def coinChange(coins, amount):
    coins.sort(reverse=True)
    result = {}
    if amount in coins:
        return amount
    else:
        for i in coins:
            number = amount//i
            amount = amount%2
            result[coins[0]] = number
            coins.pop(0)
            print(amount)
    print(result)


coinChange([2,1,10,5],15)

