def solution_1(prices: list[int]) -> int:
    low, max_profit = float("inf"), 0
    for n in prices:
        low = min(low, n)
        max_profit = max(max_profit, n - low)
    return max_profit
