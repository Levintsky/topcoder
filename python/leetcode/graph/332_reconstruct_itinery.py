"""
332. Reconstruct Itinerary (Euler Path) (Medium)

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
"""

"""
Euler Path:
1 whole way, plus out circles
1-2-3-4-5
with 2-....-2 back
so recursive and iterative dfs works

Solution 1: DFS
go until stuck, retreat
the order to try first can be alphabetical

Iterative version: Easier to understand
1. reverse sort, because we will pop right
  'A': ['D', 'C', 'B']
2. 
"""

import collections


class Solution(object):
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += (b,)
        route, stack = [], ["JFK"]
        while stack:
            while targets[stack[-1]]:
                stack += (targets[stack[-1]].pop(),)
            route += (stack.pop(),)
        return route[::-1]

    def findItinerary2(self, tickets):
        """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
        # Back-tracking plays an important role
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += (b,)
        print(targets)
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
            print(route)

        visit("JFK")
        return route[::-1]

    def solve2(self, tickets):
        edge_list = {}
        for ticket in tickets:
            src, dest = ticket
            if src not in edge_list:
                edge_list[src] = [dest]
            else:
                edge_list[src].append(dest)
            if dest not in edge_list:
                edge_list[dest] = []

        for src in edge_list.keys():
            edge_list[src].sort(reverse=True)

        curr = "JFK"
        result = [curr]
        while len(edge_list[curr]) > 0:
            dest = edge_list[curr][-1]
            if len(edge_list[curr]) == 1 or len(edge_list[dest]) != 0:
                edge_list[curr].pop()
                result.append(dest)
                curr = dest
            else:
                tmp = edge_list[curr].pop()
                tmp2 = edge_list[curr].pop()
                edge_list[curr].append(tmp)
                result.append(tmp2)
                curr = tmp2
            print(result)
        return result


if __name__ == "__main__":
    a = Solution()
    # print a.findItinery2([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    # print a.solve2([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    # print a.findItinery2([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
    # print a.solve2([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
    # print a.findItinery2([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
    # print a.findItinery2([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
    # print a.solve2([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
    # print a.findItinery2([["JFK","1"],["1","JFK"],["2","JFK"],['JFK','2']])
    # print a.solve2([["JFK","1"],["1","JFK"],["2","JFK"],['JFK','2']])
    # print(a.findItinerary([['JFK', 'A'],['A','C'], ['C','D'], ['D', 'A'], ['D','B'],['B','C'], ['C','JFK'], ['JFK','D'] ]))
    array = [
        ["JFK", "A"],
        ["A", "Z"],
        ["Z", "A"],
        ["A", "B"],
        ["B", "Y"],
        ["Y", "B"],
        ["B", "C"],
    ]
    print(a.findItinerary(array))
    # print(a.solve2([['JFK', 'A'],['A','C'], ['C','D'], ['D', 'A'], ['D','B'],['B','C'], ['C','JFK'], ['JFK','D'] ]))
