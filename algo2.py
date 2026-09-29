import numpy as np

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
    return float(dot_product / (norm_v1 * norm_v2))

# Example usage:
vec_a = np.array([0.15, 0.82, -0.34, 0.55])
vec_b = np.array([0.18, 0.79, -0.31, 0.50])
print("Similarity Score:", round(cosine_similarity(vec_a, vec_b), 4))

import torch
import torch.nn.functional as F

def scaled_dot_product_attention(q, k, v, mask=None):
    d_k = q.size(-1)
    # Compute attention scores: (batch, seq_len, seq_len)
    scores = torch.matmul(q, k.transpose(-2, -1)) / (d_k ** 0.5)
    
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float("-inf"))
        
    weights = F.softmax(scores, dim=-1)
    output = torch.matmul(weights, v)
    return output, weights

# Example: (batch=1, tokens=3, embed_dim=4)
torch.manual_seed(42)
Q = torch.randn(1, 3, 4)
K = torch.randn(1, 3, 4)
V = torch.randn(1, 3, 4)

output, weights = scaled_dot_product_attention(Q, K, V)
print("Attention Output Shape:", output.shape)
print("Attention Weights:\n", weights)

def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  # Return the index if found
    return -1  # Return -1 if not found

def sentinel_linear_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
        
    last = arr[n - 1]
    arr[n - 1] = target  # Set sentinel
    
    i = 0
    while arr[i] != target:
        i += 1
        
    arr[n - 1] = last  # Restore original last element
    
    if i < n - 1 or arr[n - 1] == target:
        return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

def ternary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
            
        if target < arr[mid1]:
            high = mid1 - 1
        elif target > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
            
    return -1

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
            
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
            
    if arr[prev] == target:
        return prev
    return -1

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
            
        # Estimate position formula
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))
        
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
            
    return -1


def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0
        
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2
        
    # Perform binary search on the found range
    low, high = i // 2, min(i, n - 1)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


