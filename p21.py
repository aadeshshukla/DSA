def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    # dp[w] will hold the maximum value achievable with capacity w
    dp = [0] * (capacity + 1)

    for i in range(n):
        wt = weights[i]
        val = values[i]
        # Traverse backward to ensure each item is used at most once
        for w in range(capacity, wt - 1, -1):
            dp[w] = max(dp[w], dp[w - wt] + val)

    return dp[capacity]

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
max_capacity = 7

print(knapsack(weights, values, max_capacity))  # Output: 9 (items with weights 3 & 4)
