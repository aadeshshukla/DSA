def move_zeros_to_end(nums):
    i=0
    for j in range(len(nums)):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
    return nums
x=[0,1,2,0,3]
print(move_zeros_to_end(x))
# time complexity O(n)
# space complexity O(1)