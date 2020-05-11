"""
1443. Minimum Time to Collect All Apples in a Tree (Medium)

Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend in order to collect all apples in the tree starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [fromi, toi] means that exists an edge connecting the vertices fromi and toi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple, otherwise, it does not have any apple.

 

Example 1:



Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
Example 2:



Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
Example 3:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0
 

Constraints:

1 <= n <= 10^5
edges.length == n-1
edges[i].length == 2
0 <= fromi, toi <= n-1
fromi < toi
hasApple.length == n
"""

class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        memo = {}
        for i, j in edges:
            if i not in memo:
                memo[i] = []
            memo[i].append(j)
        self.result = 0
        print(memo)
        
        def parse(node):
            # given: node id
            # return: True/False, n
            if node not in memo: # leaf node
                if hasApple[node]:
                    return True, 2
                else:
                    return False, 0
            flag = hasApple[node]
            result = 0
            for child in memo[node]:
                f, r = parse(child)
                if f:
                    flag = True
                    result += r
            print(node, flag, result)
            if node == 0:
                return True, result
            if flag and result == 0: # special case only self
                return True, 2
            if flag:
                return True, result + 2
            else:
                return False, 0
        
        _, self.result = parse(0)
        return self.result


if __name__ == "__main__":
    a = Solution()
    print(a.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]))
    print(a.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]))
    print(a.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,False,False,False,False,False]))
    print(a.minTime(4, [[0,1],[1,2],[0,3]], [True,True,True,True]))