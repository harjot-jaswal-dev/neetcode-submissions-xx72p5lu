# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        
        middle = len(lists) // 2
        left = lists[:middle]
        right = lists[middle:]

        sorted_left = self.mergeKLists(left)
        sorted_right = self.mergeKLists(right)

        def mergeHelper(sorted_left, sorted_right):

            dummy = ListNode(0)
            current = dummy

            left = sorted_left
            right = sorted_right

            while left and right:
                if left.val <= right.val:
                    current.next = left
                    current = current.next
                    left = left.next
                else:
                    current.next = right
                    current = current.next
                    right = right.next
            
            if left:
                current.next = left
            else:
                current.next = right
            
            return dummy.next
        return mergeHelper(sorted_left, sorted_right)
