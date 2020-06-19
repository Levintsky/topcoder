"""
1136. Parallel Courses (Hard)

There are N courses, labelled from 1 to N.

We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.

In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.

 

Example 1:



Input: N = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: 
In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.
Example 2:



Input: N = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: 
No course can be studied because they depend on each other.
 

Note:

1 <= N <= 5000
1 <= relations.length <= 5000
relations[i][0] != relations[i][1]
There are no repeated relations in the input.
"""

class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        in_degree = [0] * (N+1)
        memo = {}
        for i, j in relations:
            if i not in memo:
                memo[i] = []
            memo[i].append(j)
            in_degree[j] += 1
        
        # find 0-degree
        q = collections.deque()
        for i, item in enumerate(in_degree):
            if item == 0:
                q.append(i)
                
        step = 0
        while len(q) > 0:
            q2 = collections.deque()
            while len(q) > 0:
                item = q.popleft()
                if item in memo:
                    for i in memo[item]:
                        in_degree[i] -= 1
                        if in_degree[i] == 0:
                            q2.append(i)
            q = q2
            step += 1
        if in_degree.count(0) == N+1:
            return step
        else:
            return -1