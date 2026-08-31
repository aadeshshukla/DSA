def merge_two_sorted_arrays(arr1,m,arr2,n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1

a=[1, 3, 5, 0, 0, 0]
b=[2, 4, 6]
merge_two_sorted_arrays(a, 3, b, 3)
print(a)

# exams sar par hai 
