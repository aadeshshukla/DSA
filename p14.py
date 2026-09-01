# DSA Patterns
# Common patterns used in Data Structures and Algorithms
# two pointers pattern(slow and fast pointer)
# sliding window pattern
# merge intervals pattern
# hash map pattern
# binary search pattern
# dynamic programming pattern
# recursion pattern
# Example problems
# 1. Two Sum
# 2. Valid Parentheses
# 3. Move zeros to end
# 4. Merge Intervals    
# 5. Longest Substring Without Repeating Characters
# 6. Longest Palindromic Substring
# 7. Container With Most Water
# 8. Trapping Rain Water
# 9. Coin Change
# 10. Maximum Subarray
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# test the function
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]

def valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# test the function
print(valid_parentheses("()[]{}"))  # Output: True
print(valid_parentheses("([)]"))    # Output: False

def move_zeros(nums):
    last_non_zero_found_at = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1
    return nums

# test the function 

print(move_zeros([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]

