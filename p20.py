# Problem 20: Factorial digit sum
def factorial_digit_sum(n):
    # Calculate the factorial of n
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    
    # Convert the factorial to a string and sum the digits
    digit_sum = sum(int(digit) for digit in str(factorial))
    
    return digit_sum

# test the function
if __name__ == "__main__":
    n = 100
    result = factorial_digit_sum(n)
    print(f"The sum of the digits in the factorial of {n} is: {result}")

    