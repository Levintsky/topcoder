"""
1487. Making File Names Unique (Medium)

Given an array of strings names of size n. You will create n folders in your file system such that, at the ith minute, you will create a folder with the name names[i].

Since two files cannot have the same name, if you enter a folder name which is previously used, the system will have a suffix addition to its name in the form of (k), where, k is the smallest positive integer such that the obtained name remains unique.

Return an array of strings of length n where ans[i] is the actual name the system will assign to the ith folder when you create it.

 

Example 1:

Input: names = ["pes","fifa","gta","pes(2019)"]
Output: ["pes","fifa","gta","pes(2019)"]
Explanation: Let's see how the file system creates folder names:
"pes" --> not assigned before, remains "pes"
"fifa" --> not assigned before, remains "fifa"
"gta" --> not assigned before, remains "gta"
"pes(2019)" --> not assigned before, remains "pes(2019)"
Example 2:

Input: names = ["gta","gta(1)","gta","avalon"]
Output: ["gta","gta(1)","gta(2)","avalon"]
Explanation: Let's see how the file system creates folder names:
"gta" --> not assigned before, remains "gta"
"gta(1)" --> not assigned before, remains "gta(1)"
"gta" --> the name is reserved, system adds (k), since "gta(1)" is also reserved, systems put k = 2. it becomes "gta(2)"
"avalon" --> not assigned before, remains "avalon"
Example 3:

Input: names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
Output: ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
Explanation: When the last folder is created, the smallest positive valid k is 4, and it becomes "onepiece(4)".
Example 4:

Input: names = ["wano","wano","wano","wano"]
Output: ["wano","wano(1)","wano(2)","wano(3)"]
Explanation: Just increase the value of k each time you create folder "wano".
Example 5:

Input: names = ["kaido","kaido(1)","kaido","kaido(1)"]
Output: ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
Explanation: Please note that system adds the suffix (k) to current name even it contained the same suffix before.
 

Constraints:

1 <= names.length <= 5 * 10^4
1 <= names[i].length <= 20
names[i] consists of lower case English letters, digits and/or round brackets.
"""

from collections import defaultdict


class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        # Will TLE
        # n += 1 takes too long time;
        res = []
        s = set()
        memo = {} # key to id

        for fname in names:
            # find xxx()
            if fname not in memo:
                res.append(fname)
                memo.add(fname)
            else:
                i = 1
                while True:
                    newname = '%s(%d)' % (fname, i)
                    if newname not in memo:
                        break
                    i += 1
                res.append(newname)
                memo.add(newname)
        return res


    def solve3(self, names):
        memo = defaultdict(int)
        res = []
        for n in names:
            if memo[n] > 0:
                while n+'('+ str(memo[n]) +')' in memo.keys():
                    memo[n]+=1
                res.append(n+'('+ str(memo[n]) +')')
                memo[n+'('+ str(memo[n])+')']+=1
            else:
                res.append(n)
            memo[n]+=1
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.solve3(["pes","fifa","gta","pes(2019)"]))
    print(a.solve3(["gta","gta(1)","gta","avalon"]))
    print(a.solve3(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]))
    print(a.solve3(["wano","wano","wano","wano"]))
    print(a.solve3(["kaido","kaido(1)","kaido","kaido(1)"]))
