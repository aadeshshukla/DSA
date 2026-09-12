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

