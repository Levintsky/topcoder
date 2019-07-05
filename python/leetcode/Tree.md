# Tree

## BST
- Typical questions:
	- LC-235: Lowest Common Ancestor of a Binary Search Tree
	- LC-333: Largest BST Subtree

## Traversal
- Preorder:
```python
def preorder(self, root):
    ret, q = [], root and [root]
    while q:
        node = q.pop()
        ret.append(node.val)
        q += [child for child in node.children[::-1] if child]
    return ret
```

- Postorder:
```python
def postorder(self, root):
	if not root:
        return []
    
    stack, output = [root], []
    while stack:
        root = stack.pop()
        if root:
            output.append(root.val)
            for c in root.children:
                stack.append(c)
    return output[::-1]
```

## Binary Index Tree
- http://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
- Compared to Segment Tree, requres less space and very easy to implement
- Sum: index = index - (index & (-index))
- Update: index = index + (index & (-index))
- Get sum: O(log n)
	- id: prefix tree
	- arr[1] contained in tree nodes: 1, 2, 4, 8
	- 2: 2, 4, 8
	- 3: 3, 4, 8,
	- 5: 5, 6, 8
	- 9: 9, 10, 12
	- ...
	- Run on the same level in sub-tree, then jump to 2^n
	```
	getSum(x): Returns the sum of the sub-array arr[0,...,x]
	// Returns the sum of the sub-array arr[0,...,x] using BITree[0..n], which is constructed from arr[0..n-1]
	1) Initialize the output sum as 0, the current index as x+1.
	2) Do following while the current index is greater than 0.
	...a) Add BITree[index] to sum
	...b) Go to the parent of BITree[index].  The parent can be obtained by removing
	     the last set bit from the current index, i.e., index = index - (index & (-index))
	3) Return sum.
	```
	<img src="/python/leetcode/images/BITSum.png" alt="drawing" width="500"/>

- Update: O(log n)
	```
	update(x, val): Updates the Binary Indexed Tree (BIT) by performing arr[index] += val
	// Note that the update(x, val) operation will not change arr[].  It only makes changes to BITree[]
	1) Initialize the current index as x+1.
	2) Do the following while the current index is smaller than or equal to n.
	...a) Add the val to BITree[index]
	...b) Go to parent of BITree[index].  The parent can be obtained by incrementing
	     the last set bit of the current index, i.e., index = index + (index & (-index))
	```
	<img src="/python/leetcode/images/BITUpdate12.png" alt="drawing" width="500"/>

- LC-543: Diameter of Binary Tree
- LC-1080: Insufficient Nodes in Root to Leaf Paths

## Encode, Decode
- LC-428: Serialize and Deserialize N-ary Tree
- LC-431: Encode N-ary Tree to Binary Tree
