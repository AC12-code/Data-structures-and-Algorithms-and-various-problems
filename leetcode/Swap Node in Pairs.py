# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        lol = wow = ListNode(0)                        #creating a new list
        
        if head is None or head.next is None:
            return head
        leg = temp = head
        
        while temp is not None and leg is not None:                  #adding values to the new list in already
            temp = temp.next                                                        #swapped format
            if temp is not None:                                                     #i.e(adding the next values first and the
                wow.next = ListNode(temp.val)                               #first values after it.
                wow = wow.next                                               #e.g:  [1,2],leg=1,temp=2
                                                                                          #adding  value of temp first and then leg
                                                                                          # to the newlist
            if leg is not None:
                wow.next = ListNode(leg.val)
                wow = wow.next      
                leg = leg.next
            if temp is not None:
                temp = temp.next
            if leg is not None:
                leg = leg.next
            
        return lol.next
