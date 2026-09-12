# 1. Two Pointers & In-Place Modification
# Two Sum II (Input Array Is Sorted): Find two numbers that add up to a target using $O(1)$ extra space.

def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left, right] 
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Explanation:
# This function uses the two-pointer technique to find two numbers in a sorted array that add up to a specific target.
# we are taking two pointers, one starting from the beginning (left) and the other from the end (right) of the array.
# We calculate the sum of the numbers at these two pointers. If the sum equals the target
# we return the indices. If the sum is less than the target, we move the left pointer to the right to increase the sum.

# test cases
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([2, 3, 4], 6))
print(two_sum([-1, 0], -1))


# if array is not sorted then we can use hashmap to solve the problem in O(n) time complexity and O(n) space complexity.
class HashMap:
    def __init__(self):
        self.map = {}

    def set(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map.get(key)

def two_sum_unsorted(nums, target):
    hashmap = HashMap()
    for i, num in enumerate(nums):
        complement = target - num
        if hashmap.get(complement) is not None:
            return [hashmap.get(complement), i]
        hashmap.set(num, i)
    return []

# test cases
print(two_sum_unsorted([2, 7, 11, 15], 9))
print(two_sum_unsorted([3, 2, 4], 6))
print(two_sum_unsorted([3, 3], 6))

# Remove Duplicates from Sorted Array: Modify the array in-place so unique elements appear first; return the count.

def remove_duplicates(nums):
    if not nums:
        return 0
    write_index = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1
    return write_index

# Explanation:
# This function removes duplicates from a sorted array in-place. 
# It uses two pointers: one for reading through the array and another for writing the unique elements.
# The write pointer is used to place the unique elements at the beginning of the array.
# The function returns the count of unique elements, and the first part of the array will contain these unique elements.


# test cases
print(remove_duplicates([1, 1, 2]))  # Output: 2,
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))  # Output: 5


