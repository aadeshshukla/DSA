# length of longest substring
a="abccabbcaaabc"
def longest_sub_string(s):
    left=0
    char_set=set()
    max_length=0
    while left<len(s):
        if s[left] not in char_set:
            char_set.add(s[left])
            max_length=max(max_length,len(char_set))
            left+=1
        else:
            char_set.remove(s[left])
            left+=1
    
    return max_length

print(longest_sub_string(a))
