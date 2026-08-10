def rev_list(head):
    prev=None
    current=head
    while current:
        next=current.next
        current.next=prev
        prev=current
        current=next
    return prev
# time complexity O(n)
# space complexity O(1)


def merge_two_sorted_lists(l1, l2):
    dummy=ListNode(0)
    current=dummy
    while l1 and l2:
        if l1.val<l2.val:
            current.next=l1
            l1=l1.next
        else:
            current.next=l2
            l2=l2.next
        current=current.next
    if l1:
        current.next=l1
    if l2:
        current.next=l2
    return dummy.next
# time complexity O(n+m)
# space complexity O(1)
# runtime is 3ms , lets do it in 0ms

def merge_two_sorted_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val<l2.val:
        l1.next=merge_two_sorted_lists(l1.next,l2)
        return l1
    else:
        l2.next=merge_two_sorted_lists(l1,l2.next)
        return l2