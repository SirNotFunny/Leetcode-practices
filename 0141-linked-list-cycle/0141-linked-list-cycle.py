# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #so... the pos here is the next position that the last value will go to when it reached null, you would have to detect if it loop or not
        slow, fast = head, head #initializing 2 pts
        while fast and fast.next: #loop til end of list and to make sure that fast.next isnt a null
            slow = slow.next #slower pt move by 1
            fast = fast.next.next #faster pt move by 2
            if slow == fast: # in the loop, the fast pointer will always meet a slow pointer at one point
                return True
        return False