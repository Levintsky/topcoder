"""
431. Encode N-ary Tree to Binary Tree (Hard)

Design an algorithm to encode an N-ary tree into a binary tree 
and decode the binary tree to get the original N-ary tree. An 
N-ary tree is a rooted tree in which each node has no more 
than N children. Similarly, a binary tree is a rooted tree in 
which each node has no more than 2 children. There is no 
restriction on how your encode/decode algorithm should work. 
You just need to ensure that an N-ary tree can be encoded to 
a binary tree and this binary tree can be decoded to the 
original N-nary tree structure.

For example, you may encode the following 3-ary tree to a 
binary tree in this way:

Note that the above is just an example which might or might 
not work. You do not necessarily need to follow this format, so 
please be creative and come up with different approaches yourself. 

Note:

N is in the range of [1, 1000]
Do not use class member/global/static variables to store 
states. Your encode and decode algorithms should be stateless.
"""


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        
        :type root: Node
        :rtype: TreeNode
        """
        if root is None:
            return None
        broot = TreeNode(root.val)
        node = broot
        for i, child in enumerate(root.children):
            new_node = self.encode(child)
            if i == 0:
                broot.left = new_node
                node = broot.left
            else:
                node.right = new_node
                node = node.right
        return broot

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        
        :type data: TreeNode
        :rtype: Node
        """
        if data is None:
            return None
        root = Node(data.val, [])
        if data.left is not None:
            new_node = self.decode(data.left)
            root.children.append(new_node)

            n = data.left.right
            while n is not None:
                new_node = self.decode(n)
                root.children.append(new_node)
                n = n.right
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))

if __name__ == "__main__":
    n1 = Node(1, [])
    n2 = Node(2, [])
    n3 = Node(3, [])
    n4 = Node(4, [])
    n5 = Node(5, [])
    n6 = Node(6, [])
    n1.children = [n3, n2, n4]
    n3.children = [n5, n6]
    codec = Codec()
    b_root = codec.encode(n1)
    n_root = codec.decode(b_root)