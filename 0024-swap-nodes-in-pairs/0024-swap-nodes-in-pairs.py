# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:

            first = prev.next
            second = first.next

            # Swap the nodes
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev to the end of the swapped pair
            prev = first

        return dummy.next