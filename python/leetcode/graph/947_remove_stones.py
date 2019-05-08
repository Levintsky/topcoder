"""
947. Most Stones Removed with Same Row or Column (Medium)

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0

Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
"""

"""
Problem:
we can remove a stone if and only if,
there is another stone in the same column OR row.
We try to remove as many as stones as possible.

Find more details in chinese on the jianshu

One sentence to solve:
Connected stones can be reduced to 1 stone,
the maximum stones can be removed = stones number - islands number.
so just count the number of "islands".

1. Connected stones
Two stones are connected if they are in the same row or same col.
Connected stones will build a connected graph.
It's obvious that in one connected graph,
we can't remove all stones.

We have to have one stone left.
An intuition is that, in the best strategy, we can remove until 1 stone.

I guess you may reach this step when solving the problem.
But the important question is, how?

2. A failed strategy
Try to remove the least degree stone
Like a tree, we try to remove leaves first.
Some new leaf generated.
We continue this process until the root node left.

However, there can be no leaf.
When you try to remove the least in-degree stone,
it won't work on this "8" like graph:
[[1, 1, 0, 0, 0],
[1, 1, 0, 0, 0],
[0, 1, 1, 0, 0],
[0, 0, 1, 1, 1],
[0, 0, 0, 1, 1]]

The stone in the center has least degree = 2.
But if you remove this stone first,
the whole connected stones split into 2 parts,
and you will finish with 2 stones left.

3. A good strategy
In fact, the proof is really straightforward.
You probably apply a DFS, from one stone to next connected stone.
You can remove stones in reversed order.
In this way, all stones can be removed but the stone that you start your DFS.

One more step of explanation:
In the view of DFS, a graph is explored in the structure of a tree.
As we discussed previously,
a tree can be removed in topological order,
from leaves to root.

4. Count the number of islands
We call a connected graph as an island.
One island must have at least one stone left.
The maximum stones can be removed = stones number - islands number

The whole problem is transferred to:
What is the number of islands?

You can show all your skills on a DFS implementation,
and solve this problem as a normal one.

5. Unify index
Struggle between rows and cols?
You may duplicate your codes when you try to the same thing on rows and cols.
In fact, no logical difference between col index and rows index.

An easy trick is that, add 10000 to col index.
So we use 0 ~ 9999 for row index and 10000 ~ 19999 for col.

6. Search on the index, not the points
When we search on points,
we alternately change our view on a row and on a col.

We think:
a row index, connect two stones on this row
a col index, connect two stones on this col.

In another view：
A stone, connect a row index and col.

Have this idea in mind, the solution can be much simpler.
The number of islands of points,
is the same as the number of islands of indexes.

7. Union-Find
I use union find to solve this problem.
As I mentioned, the elements are not the points, but the indexes.

for each point, union two indexes.
return points number - union number
Copy a template of union-find,
write 2 lines above,
you can solve this problem in several minutes.

Complexity
union and find functions have worst case O(N), amortize O(1)
The whole union-find solution with path compression,
has O(N) Time, O(N) Space

If you have any doubts on time complexity,
please refer to wikipedia first.
"""

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        row_memo = {}
        col_memo = {}
        class_list = [] # class_id to parent
        for i, j in stones:
            # print(i, j)
            row_cls = row_memo.get(i, len(class_list))
            col_cls = col_memo.get(j, len(class_list))
            if row_cls == col_cls and row_cls < len(class_list):
                continue
            elif row_cls == col_cls and row_cls == len(class_list):
                row_memo[i] = len(class_list)
                col_memo[j] = len(class_list)
                class_list.append(-1)
            elif row_cls == len(class_list) or col_cls == len(class_list):
                cls_label = min(row_cls, col_cls)
                row_memo[i] = cls_label
                col_memo[j] = cls_label
            else:
                # union find
                while class_list[row_cls] != -1:
                    row_cls = class_list[row_cls]
                while class_list[col_cls] != -1:
                    col_cls = class_list[col_cls]
                if row_cls != col_cls:
                    min_ = min(row_cls, col_cls)
                    max_ = max(row_cls, col_cls)
                    if max_ != min_:
                        class_list[max_] = min_
        return len(stones) - class_list.count(-1)

    def solve2(self, points):
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        for i, j in points:
            union(i, ~j)
        return len(points) - len({find(x) for x in UF})


if __name__ == "__main__":
    a = Solution()
    """
    print(a.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
    print(a.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
    print(a.removeStones([[0,0]]))
    print(a.removeStones([[1,0],[0,1],[1,1]]))
    print(a.removeStones([[0,1],[1,2],[1,3],[3,3],[2,3],[0,2]]))
    print(a.removeStones([[3,2],[0,0],[3,3],[2,1],[2,3],[2,2],[0,2]]))
    """
    print(a.solve2([[1,0],[0,1],[1,1]]))
