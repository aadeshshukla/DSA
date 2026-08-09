l1=[1,3,5,7,9]
l2=[10,8,6,4,2]
def merge_two_sorted_lists(a,b):
    result=[]
    i=0
    j=len(b)-1
    while i<len(a) and j>=0:
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j-=1
    while i<len(a):
        result.append(a[i])
        i+=1
    while j>=0:
        result.append(b[j])
        j-=1
    return result

print(merge_two_sorted_lists(l1,l2))
# time complexity O(n)
# space complexity O(n)

x=[1,2,3,4,5]
y=[6,7,8,9,10]
# print(merge_two_sorted_lists(x,y)) this will not give correct output
# because the second list is not sorted in descending order
def merge_two_sorted_lists(a,b):
    result=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
    while i<len(a):
        result.append(a[i])
        i+=1
    while j<len(b):
        result.append(b[j])
        j+=1
    return result

print(merge_two_sorted_lists(x,y))
# time complexity O(n)
# space complexity O(n)

# reverse a list 
def reverse_list(lst):
    start=0
    end=len(lst)-1
    while start<end:
        lst[start],lst[end]=lst[end],lst[start]
        start+=1
        end-=1
    return lst
x=[1,2,3,4,5]
print(reverse_list(x))
# time complexity O(n)
# find unique elements in a sorted array 
nums=[1,1,2,2,3,3,3,4,5,5]
def remove_duplicates(nums):
    i=1
    k=0
    for i in range(len(nums)):
        if nums[k]!=nums[i]:
            k+=1
            nums[k]=nums[i]
            
    return k+1

print(remove_duplicates(nums))
# space complexity O(1)


