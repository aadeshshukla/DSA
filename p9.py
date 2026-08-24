def remove_duplicates(arr):
    result=[]
    for i in arr:
        if i not in result:
            result.append(i)
    return result

lst=[1,2,3,4,5,1,2,3]
print(remove_duplicates(lst))
# time complexity is O(n^2) because of the nested loop created by the "in" operator inside the for loop.

def remove_duplicates(arr):

    return list(set(arr))

lst=[1,2,3,4,5,1,2,3]
print(remove_duplicates(lst))

# time complexity is O(n) because the set data structure has an average time complexity of O(1) for insertions and lookups,
#  and converting the set back to a list takes O(n) time.

# sorted array
def remove_duplicates(arr):
    result = [arr[0]]

    for j in range(1, len(arr)):
        if arr[j] != result[-1]:
            result.append(arr[j])

    return result

lst=[1,2,3,4,5,6,6,7,8,9,9]
print(remove_duplicates(lst))

# time complexity is O(n) because we are iterating through the array once and performing constant time operations for each element.