"""
1019. Next Greater Node In Linked List (Medium)

We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

 

Example 1:

Input: [2,1,5]
Output: [5,5,0]
Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
Example 3:

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
 

Note:

1 <= node.val <= 10^9 for each node in the linked list.
The given list has length in the range [0, 10000].
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def nextLargerNodes(self, head: ListNode) -> List[int]:
    def nextLargerNodes(self, array):
        """
        n = head

        if n is None: return result
        
        # step 1: list to array
        array = []
        while n is not None:
            array.append(n.val)
            n = n.next
        """
        stack = []
        result = []
        # step 2:
        stack.append((0, array[0]))
        result = [0] * len(array)
        for idx in range(1, len(array)):
            item = array[idx]
            if item <= stack[-1][1]:
                stack.append((idx, item))
            else:
                while len(stack) > 0 and stack[-1][1] < item:
                    idx2, _ = stack.pop()
                    result[idx2] = item
                stack.append((idx, item))
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.nextLargerNodes([1, 7, 5, 1, 9, 2, 5, 1]))
    # print(a.nextLargerNodes([2,1,5]))
