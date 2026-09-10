# Hash Map 
# A hash map is a data structure that stores key-value pairs. 
# It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

class HashMap:
    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                self.map[index][i] = (key, value)
                return
        self.map[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.map[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                del self.map[index][i]
                return

# dsa problems on hashmap 
# problem 1: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# example: Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

def two_sum(nums, target):
    hashmap = HashMap()
    for i, num in enumerate(nums):
        complement = target - num
        if hashmap.get(complement) is not None:
            return [hashmap.get(complement), i]
        hashmap.set(num, i)
    return []

