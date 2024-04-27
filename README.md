# Merge Two Sorted Lists

## Problem Statement
You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

### Example:
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

## Constraints
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

## Approach
We can solve this problem iteratively by comparing the values of the nodes from both lists and merging them into a new list. We'll maintain two pointers, one for each list, and a pointer to the current node of the merged list. We'll compare the values of the nodes pointed by the two pointers and append the smaller value node to the merged list. Then, we'll move the pointer of the list whose node was appended to the merged list. We'll repeat this process until we reach the end of one of the lists. Finally, if there are any remaining nodes in the non-empty list, we'll append them to the merged list. 

## Algorithm
1. Initialize a dummy node `dummy` and a pointer `current` to it.
2. While both `list1` and `list2` are not empty, do:
   - Compare the values of the nodes pointed by `list1` and `list2`.
   - Append the smaller value node to `current.next`.
   - Move the pointer of the list whose node was appended.
3. If there are any remaining nodes in `list1` or `list2`, append them to `current.next`.
4. Return `dummy.next`, which is the head of the merged linked list.

## Time Complexity
The time complexity of this algorithm is O(n), where n is the total number of nodes in `list1` and `list2`, as we traverse both lists once.

## Space Complexity
The space complexity is O(1) as we are not using any extra space except for a few pointers.
```
