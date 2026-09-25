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

def quicksort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

# Example
unsorted = [33, 10, 59, 27, 41, 88, 12]
print("Sorted:", quicksort(unsorted))  # Output: [10, 12, 27, 33, 41, 59, 88]

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph: dict, start: str) -> list[str]:
    visited = set([start])
    queue = deque([start])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def dfs(graph: dict, start: str, visited: set = None) -> list[str]:
    if visited is None:
        visited = set()
    order = []
    
    if start not in visited:
        visited.add(start)
        order.append(start)
        for neighbor in graph[start]:
            order.extend(dfs(graph, neighbor, visited))
    return order

print("BFS Order:", bfs(graph, 'A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']
print("DFS Order:", dfs(graph, 'A'))  # Output: ['A', 'B', 'D', 'E', 'F', 'C']
