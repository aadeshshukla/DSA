print("hello world!")
# not well enough today 
# hope!!!....    .    .

# I'm back 
# reverse an array 
def rev_arr(arr):
    i=0
    j=len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

lst=[1,2,3,4,5]
print(rev_arr(lst))
