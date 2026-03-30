# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        org_values = []
        reversed_val = []

        head1 = head
        curr = head
        prev = None

        while head:
            org_values.append(head.val)
            head = head.next
            
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        
        while prev:
            reversed_val.append(prev.val)
            prev = prev.next
        
        
        for i in range(len(org_values)):
            if org_values[i] != reversed_val[i]:
                return False
        return True