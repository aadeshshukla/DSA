l1=[1,3,5,7,9]
l2=[10,8,6,4,2]

def merge_two_sorted_lists(a,b):
    result = []
    i = 0
    j=len(b)-1
    while i < len(a) and j >= 0:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j -= 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j >= 0:
        result.append(b[j])
        j -= 1
    return result

print(merge_two_sorted_lists(l1,l2))
    