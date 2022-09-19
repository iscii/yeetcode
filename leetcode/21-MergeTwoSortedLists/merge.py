# 9/19/2022
# Runtime: 14 ms
# Memory Usage: 13.5 MB

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        #LISTS ARE LINKEDLISTS
        #go through each list using while loops (nested loop - O(n^2))
        #instead of incrementing, always look at the head of the two lists
        #remove the min head and append to resulting list

        #*NOTE: address base cases first thing when starting the code

        #initial base case
        if(list1 is None and list2 is None): return None
        if(list1 is None): return list2
        if(list2 is None): return list1

        #initial case to init resulting list
        if(list1.val > list2.val):
            result = ListNode(list2.val)
            list2 = list2.next
        else:
            result = ListNode(list1.val)
            list1 = list1.next
        
        cur = result #so that result can retain its role as the head of the linkedlist cos there's no prev
        
        while(not(list2 is None and list1 is None)): #had a lot of trouble from this conditional. while(list1 is not None and list2 is not None): does not work -> it basically does an or instead of an and. why?
            #base case None
            if(list1 is None):
                cur.next = list2
                cur = cur.next
                list2 = list2.next
                continue
            if(list2 is None):
                cur.next = list1
                cur = cur.next
                list1 = list1.next
                continue
            if(list1.val > list2.val):
                cur.next = list2
                cur = cur.next
                list2 = list2.next
            else:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
                
        return result
            
s = Solution

c1 = ListNode(4)
b1 = ListNode(2, c1)
a1 = ListNode(1, b1)

c2 = ListNode(4)
b2 = ListNode(3, c2)
a2 = ListNode(1, b2)

b = s.mergeTwoLists(s, a1, a2)

while(b is not None):
    print(f"{b.val} ")
    b = b.next
