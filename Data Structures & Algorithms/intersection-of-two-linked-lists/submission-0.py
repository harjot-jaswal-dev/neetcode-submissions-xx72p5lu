# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1 = headA
        node2 = headB

        def get_length(list1, list2):
            length1 = 0
            length2 = 0

            while list1:
                length1 += 1
                list1 = list1.next
            
            while list2:
                length2 += 1
                list2 = list2.next
            return length1, length2

        length1, length2 = get_length(node1, node2)
        curr1 = headA
        curr2 = headB

        if length1 > length2:
            for _ in range(length1 - length2):
                curr1 = curr1.next
        else:
            for _ in range(length2 - length1):
                curr2 = curr2.next
        
        while curr1 and curr2:
            if curr1 == curr2:
                return curr1
            else:
                curr1 = curr1.next
                curr2 = curr2.next
        return None