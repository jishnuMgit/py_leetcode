# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         newarr=[]
#         rang=len(head)
#         for i in range(rang):
#             print('i,rand',i,rang)
#             print(i)
#             if head[i] !=head[-1] :
                
#                 if head[i] != head[i+1]:
#                     newarr.append(head[i])
#             elif i== rang - 1:
#                  newarr.append(head[i])

#         return newarr          

class Solution(object):
    def deleteDuplicates(self, head):

        current = head

        while current is not None and current.next is not None:

            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
solution=Solution()    
print(solution.deleteDuplicates([1,1,2]))   
