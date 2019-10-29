"""
1233. Remove Sub-Folders from the Filesystem (Medium)

Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".
Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
 

Constraints:

1 <= folder.length <= 4 * 10^4
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'
folder[i] always starts with character '/'
Each folder name is unique.
"""

class TrieNode():
	def __init__(self):
		self.end = False
		self.next = {}

class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort(key=lambda x:len(x))
        root = TrieNode()
        result = []
        for f in folder:
        	tmplist = f.split("/")
        	# print(len(tmplist), tmplist)
        	node = root
        	flag = True
        	for i, tmp in enumerate(tmplist):
        		if node.end:
        			flag = False
        			break
        		if tmp not in node.next:
        		    node.next[tmp] = TrieNode()
        		node = node.next[tmp]
        		if i == len(tmplist) - 1:
        			node.end = True
        	if flag:
        		result.append(f)
        return result



if __name__ == "__main__":
	a = Solution()
	print(a.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
	print(a.removeSubfolders(["/a","/a/b/c","/a/b/d"]))
	print(a.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))