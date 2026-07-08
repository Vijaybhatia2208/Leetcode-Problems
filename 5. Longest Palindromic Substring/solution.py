# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
    
        arr1 = []
        arr2 = []
        
        while head.next :
            arr1.append(head.val)
            head = head.next
        
        arr1.append(head.val)

        head = l2

        while head.next :
            arr2.append(head.val)
            head = head.next
        
        arr2.append(head.val)

        n = len(arr1)
        m = len(arr2)

        i = 0
        j = 0
        carry = 0
        helper = []
        while i < n or j < m:
            x=0
            y=0
            if i<n:
                x= arr1[i]
            if j<m:
                y= arr2[j]

            sum = x+y+carry

            helper.append(sum%10)
            print(sum, sum%10, carry, helper)


            if sum > 9:
                carry = 1
            else :
                carry = 0
            i+=1
            j+=1
        
        if carry > 0:
            helper.append(carry)
        
        answer = []
        for i in range(0, len(helper)):
            link = ListNode(helper[i])
            answer.append(link)

        for i in range(0, len(answer )):
            if i == len(answer )-1:
                break
            
            answer[i].next = answer[i+1]

        return answer[0]
