# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        lis = []
        llis=[]
        new = lol = ListNode(0)
        count = 1
        if head is None or k == 0 or k == 1:
            return head
        leg = temp = head
        while leg is not None:
            llis.append(leg.val)
            leg = leg.next
        lens = len(llis)
        
        while temp is not None:
            lis.append(temp.val)
            temp = temp.next
            count+=1
            if temp is None:
                break
            if count == k:
                lis.append(temp.val)
                
                for i in lis[::-1]:
                    new.next = ListNode(i)
                    new  = new.next
                count = 1
                lis.clear()
                temp = temp.next
        c = lens%k 
        for j in range(c):
            new.next = ListNode(llis[-c])
            new = new.next
            c-=1
        return lol.next
