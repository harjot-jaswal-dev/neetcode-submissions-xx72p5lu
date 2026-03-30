# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # linked list so need to use next pointer
        # lets do merge sort

        # base case
        if len(lists) == 1:
            return lists[0] # since lists is a list of lists we need the index
        if len(lists) == 0:
            return None # if empty return empty lists of lists

        middle = len(lists) // 2
        left = lists[:middle]
        right = lists[middle:]

        sorted_left = self.mergeKLists(left) # to get to 1 lists we recurse
        sorted_right = self.mergeKLists(right)

        # now we merge

        def merge(sorted_left, sorted_right):

            left = sorted_left
            right = sorted_right
            # dummy node
            dummy = ListNode(0)
            current = dummy

            while left and right: # if we have a valid pos on both linked lists
                if left.val <= right.val:
                    current.next = left
                    current = current.next
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                    current = current.next
                
            # if any are remianing/only one is executed due to how we do our code above
            if left:
                current.next = left
            else:
                current.next = right
            
            return dummy.next
        return merge(sorted_left, sorted_right)













