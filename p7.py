# remove dduplicates and return the no of unique elements 
def remove_duplicates(nums):
    i=0
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]
    return i+1

list1=[1,1,2]
print(remove_duplicates(list1))
# time complexity O(n)
# space complexity O(1)