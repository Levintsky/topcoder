'''
297. Serialize and Deserialize Binary Tree (Hard)

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
   self.val = x
   self.left = None
   self.right = None

class Codec:
  def serialize(self, root):
    """Encodes a tree to a single string.
        
    :type root: TreeNode
    :rtype: str
    """
    self.result = ""
    self.preorder(root)
    return self.result

  def preorder(self, root):
    if len(self.result) != 0:
      self.result += " "
    if root:
      self.result += str(root.val)
      self.preorder(root.left)
      self.preorder(root.right)
    else:
      self.result += "#"
    # return result

  def deserialize(self, data):
    """Decodes your encoded data to tree.
        
    :type data: str
    :rtype: TreeNode
    """
    data_l = data.split(" ")
    if len(data_l) == 1: return None
    node, i = self.helper(data_l, 0)
    return node

  def helper(self, data_l, i):
    print "i", i,
    if data_l[i] == "#":
      print "#"
      return None, i+1
    else:
      node = TreeNode(int(data_l[i]))
      # print node.val
      # print "tackle left: ", data_l[i+1]
      node.left, i = self.helper(data_l, i+1)
      # print "after left, i:", i, data_l[i]
      # print "tackle right: ", data_l[i]
      node.right, i = self.helper(data_l, i)
      # print "after both left and right", i, data_l[i]
      return node, i

if __name__ == "__main__":
  n1 = TreeNode(1)
  n2 = TreeNode(2)
  n3 = TreeNode(3)
  n4 = TreeNode(4)
  n5 = TreeNode(5)
  n1.left, n1.right = n2, n3
  n3.left, n3.right = n4, n5

  codec = Codec()
  result = codec.serialize(n1) 
  print result
  node = codec.deserialize(result)
  print node.val
  print node.left.val, node.right.val
  print node.right.left.val, node.right.right.val
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
