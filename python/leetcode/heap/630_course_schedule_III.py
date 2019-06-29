"""
630. Course Schedule III (Hard)

There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:
Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3

Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

Note:
The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.
"""

"""
Solution:
public class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses,(a,b)->a[1]-b[1]); //Sort the courses by their deadlines (Greedy! We have to deal with courses with early deadlines first)
        PriorityQueue<Integer> pq=new PriorityQueue<>((a,b)->b-a);
        int time=0;
        for (int[] c:courses) 
        {
            time+=c[0]; // add current course to a priority queue
            pq.add(c[0]);
            if (time>c[1]) time-=pq.poll(); //If time exceeds, drop the previous course which costs the most time. (That must be the best choice!)
        }        
        return pq.size();
    }
}
"""

import Queue


class Solution(object):
  def scheduleCourse(self, courses):
    """
    :type courses: List[List[int]]
    :rtype: int
    """
    courses.sort(key=lambda item: item[1])
    q = Queue.PriorityQueue()
    start = 0
    n = len(courses)
    i = 0
    cnt = 0
    while i<n:
      item, end = courses[i]
      q.put(-item)
      start += item
      cnt += 1
      while start>end:
        tmp = q.get()
        start += tmp
        cnt -= 1
      i += 1
    return cnt

if __name__ == '__main__':
  a = Solution()
  print a.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])
  print a.scheduleCourse([[5,5],[2,6],[4,6]])
  print a.scheduleCourse([[5,5],[2,100],[4,100]])
  print a.scheduleCourse([[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]])
