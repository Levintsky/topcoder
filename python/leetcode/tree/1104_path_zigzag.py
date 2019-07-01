"""
1104. Path In Zigzag Labelled Binary Tree (Easy)

In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
 

Constraints:

1 <= label <= 10^6
"""

import math

class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        n = int(math.ceil(math.log(label + 0.99, 2)))
        print(n)
        result = []
        if n % 2 == 0:
            label = 2 ** (n-1) + 2 ** n - 1 - label

        while label > 0:
            result.append(label)
            label //= 2
        result = result[::-1]
        print(result)
        for i in range(len(result)):
            if i % 2 == 1:
                result[i] = 2 ** i + 2 ** (i+1) - 1 - result[i]
        return result

if __name__ == "__main__":
    a = Solution()
    print(a.pathInZigZagTree(26))
