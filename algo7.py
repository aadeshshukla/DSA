# linear search algorithm
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Return -1 if the target is not found

# test case
if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2]
    target = 4
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")