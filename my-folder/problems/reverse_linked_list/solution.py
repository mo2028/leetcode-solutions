# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1->
        
        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        # newHead.next = head

        return newHead

        # curr = head
        # if not curr or not curr.next:
        #     return curr
        # else:
        #     newHead = self.reverseList(curr.next)
        #     newHead.next = curr
        # return curr




        
        



        






       

        











        

        