"""
797. All Paths From Source to Target (Medium)

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Note:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.
"""

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.memo = {} # node to parents
        n = len(graph)
        for i, items in enumerate(graph):
            if len(items) == 0:
                target = i
            else:
                for item in items:
                    if item not in self.memo:
                        self.memo[item] = [i]
                    else:
                    	self.memo[item].append(i)
        srcs = set()
        for i in range(n):
            if i not in self.memo:
                srcs.add(i)
        self.result = []
        # bfs backward
        def bfs(node, prev_lists):
            if node in srcs:
                for items in prev_lists:
                    self.result.append(items[::-1])
            else:
                for par in self.memo[node]:
                    lists_bak = []
                    for list_ in prev_lists:
                        tmp_list = [item for item in list_]
                        tmp_list.append(par)
                        lists_bak.append(tmp_list)
                    bfs(par, lists_bak)
        bfs(target, [[target]])
        return self.result


if __name__ == "__main__":
    a = Solution()
    print(a.allPathsSourceTarget([[1,2], [3], [3], []] ))