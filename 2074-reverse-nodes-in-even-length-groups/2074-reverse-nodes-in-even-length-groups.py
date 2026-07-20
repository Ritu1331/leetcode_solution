# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverse(self, head, k):
        prev = None
        curr = head

        while k > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k -= 1

        return prev, head, curr

    def reverseEvenLengthGroups(self, head):

        dummy = ListNode(0)
        dummy.next = head

        prev_group = dummy
        group_size = 1

        while prev_group.next:

            curr = prev_group.next

            count = 0
            temp = curr

            while temp and count < group_size:
                temp = temp.next
                count += 1

            if count % 2 == 0:

                new_head, new_tail, next_group = self.reverse(curr, count)

                prev_group.next = new_head
                new_tail.next = next_group

                prev_group = new_tail

            else:

                for _ in range(count):
                    prev_group = prev_group.next

            group_size += 1

        return dummy.next
        