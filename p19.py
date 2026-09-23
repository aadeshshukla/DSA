# dsa problems 
# problem 1: find the maximum number in an array
def find_maximum(arr):
    if not arr:
        return None  # Return None for empty array
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
    