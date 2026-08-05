# Brute Force Approach
def sum_of_digits(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum
print(sum_of_digits(12345))

# optimization
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
print(sum_of_digits(12345))

# Recursive Approach
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)
print(sum_of_digits(12345))

# Dynamic Programming
def sum_of_digits(n):
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i // 10] + (i % 10)
    return dp[n]
print(sum_of_digits(12345))

# lets understand the time complexity of each approach
# Brute Force Approach: O(n)
# optimization: O(n)
# Recursive Approach: O(n)
# Dynamic Programming: O(n)
# lets understand the space complexity of each approach
# Brute Force Approach: O(1)
# optimization: O(n)
# Recursive Approach: O(n)
# Dynamic Programming: O(n)

