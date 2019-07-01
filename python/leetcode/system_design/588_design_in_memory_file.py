'''
588. Design In-Memory File System (Hard)

Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

Example:
Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
Output:
[null,[],null,null,["a"],"hello"]
Explanation:
filesystem
Note:
You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.
'''

"""
class TrieNode(object):
    def __init__(self, s):
        self.name = s
        self.subfiles = {} # String to other tree nodes
        self.is_file = False
        self.content = None

class FileSystem(object):
    def __init__(self):
        self.root = TrieNode('')
         
    def ls(self, path):
      :type path: str
      :rtype: List[str]
      node = self.root
      # find the node
      if path != '/':
        path_list = path_list.split('/')
        path_list = path_list[1:]
        for item in path_list:
          node = node.subfiles[item]
      return node.subfiles.keys()

    def mkdir(self, path):
      :type path: str
      :rtype: void
      path_list = path.split('/')
      path_list = path_list[1:]
      node = self.root
      for item in path_list:
        if item in node.subfiles:
          node = node.subfiles[item]
        else:
          new_node = TrieNode(item)
          node.subfiles[item] = new_node
          node = new_node
          
    def addContentToFile(self, filePath, content):
      :type filePath: str
      :type content: str
      :rtype: void
      path_list = filePath.split('/')
      path_list = path_list[1:]
      node = self.root
      for item in path_list:
        if item in node.subfiles:
          node = node.subfiles[item]
        else:
          new_node = TrieNode(item)
          node.subfiles[item] = new_node
          node = new_node
      node.content = content
      node.is_file = True

    def readContentFromFile(self, filePath):
      :type filePath: str
      :rtype: str
      node = self.root
      path_list = filePath.split('/')
      path_list = path_list[1:]
      for item in path_list:
        node = node.subfiles[item]
      return node.content
"""

class TreeNode(object):
    def __init__(self):
        # self.name = name
        self.content = ""
        self.children = {}
        self.isfile = False
        
class FileSystem(object):

    def __init__(self):
        self.root = TreeNode()

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        path_list = path.split("/")
        n = self.root
        for item in path_list:
            if item == "":
                continue
            n = n.children[item]
        if n.isfile:
            return [path_list[-1]]
        tmp = list(n.children.keys())
        tmp.sort()
        return tmp

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        path_list = path.split("/")
        n = self.root
        for item in path_list:
            if item == "":
                continue
            if item not in n.children:
                n.children[item] = TreeNode()
            n = n.children[item]

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        path_list = filePath.split("/")
        n = self.root
        for item in path_list:
            if item == "":
                continue
            if item not in n.children:
                n.children[item] = TreeNode()
            n = n.children[item]
        n.content += content
        n.isfile = True

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        path_list = filePath.split("/")
        n = self.root
        for item in path_list:
            if item == "":
                continue
            n = n.children[item]
        return n.content
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

if __name__ == '__main__':
    f = FileSystem()
    f.addContentToFile("/a", "hello")
    print(f.ls("/"))
    """
    f.mkdir("/goowmfn")
    print(f.ls("/goowmfn"))
    print(f.ls("/"))
    f.mkdir("/z")
    print(f.ls("/"))
    print(f.ls("/"))
    print(f.addContentToFile("/goowmfn/c", "shetopcy"))
    print(f.ls("/z"))
    print(f.ls("/goowmfn/c"))
    print(f.ls("/goowmfn"))
    """
    """
    print('ls: ', f.ls('/'))
    f.mkdir('/a/b/c')
    f.addContentToFile("/a/b/c/d","hello")
    print('ls: ', f.ls('/'))
    print(f.readContentFromFile('/a/b/c/d'))
    """