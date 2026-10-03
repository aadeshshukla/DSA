def factorial(n: int) -> int:
    # Base case: stop condition
    if n <= 1:
        return 1
    # Recursive step
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

def fib_naive(n: int) -> int:
    if n <= 1:
        return n
    # Recomputes branches like fib(n-2) multiple times across the tree
    return fib_naive(n - 1) + fib_naive(n - 2)

# Time Complexity: O(2^n) - becomes unusable around n=35-40

def fib_memo(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Alternatively, Python's built-in decorator handles this automatically:
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cached(n: int) -> int:
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

print(fib_memo(50))  # Output: 12586269025 (instantaneous, O(n) time)

def fib_bottom_up(n: int) -> int:
    if n <= 1:
        return n

    # We only need the previous two values
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1

    return prev1

print(fib_bottom_up(50))  # O(n) time, O(1) space

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
