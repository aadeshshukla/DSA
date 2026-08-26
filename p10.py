def search_element(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

lst=[1,2,3,4,5]
target=3
print(search_element(lst,target))