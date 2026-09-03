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

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
    return merged   

# test the function
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]

def longest_substring_without_repeating_characters(s):
    char_index_map = {}
    left = 0
    max_length = 0
    for right in range(len(s)):
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length

# test the function
print(longest_substring_without_repeating_characters("abcabcbb"))  # Output: 3

def remove_duplicates_from_array(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1    


# test the function
print(remove_duplicates_from_array([1, 1, 2]))  # Output: 2
