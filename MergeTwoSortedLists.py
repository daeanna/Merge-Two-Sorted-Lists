
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start the merged list
        dummy = ListNode()
        # Create a pointer 'cur' to keep track of the current node in the merged list
        cur = dummy
        
        # Traverse both lists until one of them becomes empty
        while list1 and list2:
            # Compare the values of the current nodes in list1 and list2
            if list1.val < list2.val:
                # If the value in list1 is smaller, attach list1's node to the merged list
                cur.next = list1
                # Move list1 pointer to the next node
                list1 = list1.next
            else:
                # If the value in list2 is smaller or equal, attach list2's node to the merged list
                cur.next = list2
                # Move list2 pointer to the next node
                list2 = list2.next
                
            # Move the 'cur' pointer to the next node in the merged list
            cur = cur.next
            
        # Attach the remaining nodes from either list1 or list2 to the merged list
        cur.next = list1 if list1 else list2
        
        # Return the head of the merged list, excluding the dummy node
        return dummy.next
