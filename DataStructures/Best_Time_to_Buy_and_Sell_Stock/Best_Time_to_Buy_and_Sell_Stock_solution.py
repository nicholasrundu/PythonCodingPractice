from typing import List


def max_profit(prices: List[int]) -> int:
    profit = 0
    min_price = prices[0]
    for price in prices:
        if price < min_price:
            min_price = price
        if price - min_price > profit:
            profit = price - min_price
    return profit


assert max_profit([7, 1, 5, 3, 6, 4]) == 5
assert max_profit([7, 6, 4, 3, 1]) == 0
