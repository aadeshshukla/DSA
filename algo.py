def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# Example
nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("Index of 23:", binary_search(nums, 23))  # Output: 5
