"""
428. Serialize and Deserialize N-ary Tree (Hard)

Serialization is the process of converting a data structure or 
object into a sequence of bits so that it can be stored in a file 
or memory buffer, or transmitted across a network connection 
link to be reconstructed later in the same or another computer 
environment.

Design an algorithm to serialize and deserialize an N-ary tree. 
An N-ary tree is a rooted tree in which each node has no more 
than N children. There is no restriction on how your 
serialization/deserialization algorithm should work. You just 
need to ensure that an N-ary tree can be serialized to a string 
and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree 

as [1 [3[5 6] 2 4]]. You do not necessarily need to follow 
this format, so please be creative and come up with different 
approaches yourself.

Note:

N is in the range of [1, 1000]
Do not use class member/global/static variables to store 
states. Your serialize and deserialize algorithms should 
be stateless.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def dfs(node):
            # print(node.val)
            if node is None:
                return ""
            res = str(node.val) 
            if len(node.children) > 0:
                res += "["
                for child in node.children:
                    subres = dfs(child)
                    res += subres + " "
                res = res[:-1]
                res += "]"
            return res
        result = dfs(root)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if data == "": return None
        i = 0
        while i < len(data) and data[i] != "[":
            i += 1
        val = int(data[:i])
        node = Node(val, [])
        if i == len(data):
            return node
        rest = data[i:]
        rest = rest[1:-1] # remove outer "[]"
        restlist = rest.split(" ")
        finallist = []
        curr = ""
        for i, c in enumerate(restlist):
            if curr == "":
                curr = c
            else:
                curr += " " + c

            if curr.count("[") - curr.count("]") == 0:
                finallist.append(curr)
                curr = ""               
        # finallist.append(curr)
        for item in finallist:
            newnode = self.deserialize(item)
            node.children.append(newnode)
        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

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
    s = codec.serialize(n1)
    print(s)
    n = codec.deserialize(s)

    s = codec.serialize(None)
    print(s)

"""
Idea: preorder recursive traversal; add number of children after root val, in order to know when to terminate.
Example: The example in description is serialized as: "1,3,3,2,5,0,6,0,2,0,4,0"

class Codec {

    // Encodes a tree to a single string.
    public String serialize(Node root) {
        List<String> list=new LinkedList<>();
        serializeHelper(root,list);
        return String.join(",",list);
    }
    
    private void serializeHelper(Node root, List<String> list){
        if(root==null){
            return;
        }else{
            list.add(String.valueOf(root.val));
            list.add(String.valueOf(root.children.size()));
            for(Node child:root.children){
                serializeHelper(child,list);
            }
        }
    }

    // Decodes your encoded data to tree.
    public Node deserialize(String data) {
        if(data.isEmpty())
            return null;
        
        String[] ss=data.split(",");
        Queue<String> q=new LinkedList<>(Arrays.asList(ss));
        return deserializeHelper(q);
    }
    
    private Node deserializeHelper(Queue<String> q){
        Node root=new Node();
        root.val=Integer.parseInt(q.poll());
        int size=Integer.parseInt(q.poll());
        root.children=new ArrayList<Node>(size);
        for(int i=0;i<size;i++){
            root.children.add(deserializeHelper(q));
        }
        return root;
    }
}
"""