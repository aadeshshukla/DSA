# sliding window
# program to find the maximum sum of k consecutive elements in an array of size n
def max_sum_k_consecutive(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid input: k is larger than the array size."
    
    # Compute the sum of the first window of size k
    max_sum = sum(arr[:k])
    current_sum = max_sum
    
    # Slide the window from start to end of the array
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# test the function
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 3
    result = max_sum_k_consecutive(arr, k)
    print(f"The maximum sum of {k} consecutive elements is: {result}")
    

# program 2 : max avg of sub array of size k
def max_avg_k_consecutive(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid input: k is larger than the array size."
    
    # Compute the sum of the first window of size k
    max_sum = sum(arr[:k])
    current_sum = max_sum
    
    # Slide the window from start to end of the array
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
    
    # Calculate the maximum average
    max_avg = max_sum / k
    return max_avg

# test the function
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 3
    result = max_avg_k_consecutive(arr, k)
    print(f"The maximum average of {k} consecutive elements is: {result}")
    
    