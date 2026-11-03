import time

# 1. Unoptimized approach using lists: O(n) lookup per check -> O(n * m) overall
def find_common_unoptimized(list_a, list_b):
    common = []
    for item in list_a:
        if item in list_b:  # Linear scan through list_b every iteration
            common.append(item)
    return common

# 2. Optimized approach using sets: O(1) hash lookup -> O(n + m) overall
def find_common_optimized(list_a, list_b):
    set_b = set(list_b)    # O(m) to build the hash set
    return [item for item in list_a if item in set_b]  # O(1) membership check

# Benchmark with sample data
data_a = list(range(10_000))
data_b = list(range(5_000, 15_000))

# Test unoptimized
start = time.perf_counter()
res_unopt = find_common_unoptimized(data_a, data_b)
time_unopt = time.perf_counter() - start

# Test optimized
start = time.perf_counter()
res_opt = find_common_optimized(data_a, data_b)
time_opt = time.perf_counter() - start

print(f"Unoptimized time: {time_unopt:.4f} seconds")
print(f"Optimized time:   {time_opt:.4f} seconds")
print(f"Speedup:          {time_unopt / time_opt:.1f}x faster")
