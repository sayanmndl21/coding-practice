# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        ptr = head
        
        #check if there are k nodes
        while count < k and ptr:
            ptr= ptr.next
            count += 1
            
        if count == k:
            reversedHead = self.reverseLindedList(head,k)
            
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head
            
            
    def reverseLindedList(self, head, k):
        new_head, ptr = None, head
        
        while k:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k-=1
            
        return new_head