"""
587. Erect the Fence (Hard)

There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.

Example 1:
Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation:

Example 2:
Input: [[1,2],[2,2],[4,2]]
Output: [[1,2],[2,2],[4,2]]
Explanation:
Even you only have trees in a line, you need to use rope to enclose them. 

Note:

All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
All input integers will range from 0 to 100.
The garden has at least one tree.
All coordinates are distinct.
Input points have NO order. No order required for output.
"""

"""
There are couple of ways to solve Convex Hull problem. https://en.wikipedia.org/wiki/Convex_hull_algorithms
The following code implements Gift wrapping aka Jarvis march algorithm https://en.wikipedia.org/wiki/Gift_wrapping_algorithm and also added logic to handle case of multiple Points in a line because original Jarvis march algorithm assumes no three points are collinear.
It also uses knowledge in this problem https://leetcode.com/problems/convex-polygon . Disscussion: https://discuss.leetcode.com/topic/70706/beyond-my-knowledge-java-solution-with-in-line-explanation

public class Solution {
    public List<Point> outerTrees(Point[] points) {
        Set<Point> result = new HashSet<>();
        
        // Find the leftmost point
        Point first = points[0];
        int firstIndex = 0;
        for (int i = 1; i < points.length; i++) {
            if (points[i].x < first.x) {
                first = points[i];
                firstIndex = i;
            }
        }
        result.add(first);
        
        Point cur = first;
        int curIndex = firstIndex;
        do {
            Point next = points[0];
            int nextIndex = 0;
            for (int i = 1; i < points.length; i++) {
                if (i == curIndex) continue;
                int cross = crossProductLength(cur, points[i], next);
                if (nextIndex == curIndex || cross > 0 ||
                        // Handle collinear points
                        (cross == 0 && distance(points[i], cur) > distance(next, cur))) {
                    next = points[i];
                    nextIndex = i;
                }
            }
            // Handle collinear points
            for (int i = 0; i < points.length; i++) {
                if (i == curIndex) continue;
                int cross = crossProductLength(cur, points[i], next);
                if (cross == 0) {
                    result.add(points[i]);
                }
            }

            cur = next;
            curIndex = nextIndex;
            
        } while (curIndex != firstIndex);
        
        return new ArrayList<Point>(result);
    }
    
    private int crossProductLength(Point A, Point B, Point C) {
        // Get the vectors' coordinates.
        int BAx = A.x - B.x;
        int BAy = A.y - B.y;
        int BCx = C.x - B.x;
        int BCy = C.y - B.y;
    
        // Calculate the Z coordinate of the cross product.
        return (BAx * BCy - BAy * BCx);
    }

    private int distance(Point p1, Point p2) {
        return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
    }
}
"""

"""
Solution 2: Graham Scan
The trick is that once all points are sorted by polar angle with respect to the reference point:

For collinear points in the begin positions, make sure they are sorted by distance to reference point in ascending order.
For collinear points in the end positions, make sure they are sorted by distance to reference point in descending order.
For example:
(0, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (1, 2), (0, 2), (0, 1)
These points are sorted by polar angle
The reference point (bottom left point) is (0, 0)

In the begin positions (0, 0) collinear with (2, 0), (3, 0) sorted by distance to reference point in ascending order.
In the end positions (0, 0) collinear with (0, 2), (0, 1) sorted by distance to reference point in descending order.
Now we can run the standard Graham scan to give us the desired result.

public class Solution {

    public List<Point> outerTrees(Point[] points) {
        if (points.length <= 1)
            return Arrays.asList(points);
        sortByPolar(points, bottomLeft(points));
        Stack<Point> stack = new Stack<>(); 
        stack.push(points[0]);                      
        stack.push(points[1]);                              
        for (int i = 2; i < points.length; i++) {
            Point top = stack.pop();                                
            while (ccw(stack.peek(), top, points[i]) < 0)
                top = stack.pop();
            stack.push(top);
            stack.push(points[i]);
        }       
        return new ArrayList<>(stack);
    }                               

    private static Point bottomLeft(Point[] points) {
        Point bottomLeft = points[0];
        for (Point p : points)          
            if (p.y < bottomLeft.y || p.y == bottomLeft.y && p.x < bottomLeft.x)
                bottomLeft = p;                 
        return bottomLeft;                                                  
    }

    /**
     * @return positive if counter-clockwise, negative if clockwise, 0 if collinear
     */
    private static int ccw(Point a, Point b, Point c) {
        return a.x * b.y - a.y * b.x + b.x * c.y - b.y * c.x + c.x * a.y - c.y * a.x;       
    }

    /**
     * @return distance square of |p - q|
     */
    private static int dist(Point p, Point q) {
        return (p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y);
    }
                              
    private static void sortByPolar(Point[] points, Point r) {
        Arrays.sort(points, (p, q) -> {
            int compPolar = ccw(p, r, q);
            int compDist = dist(p, r) - dist(q, r); 
            return compPolar == 0 ? compDist : compPolar;
        });     
        // find collinear points in the end positions
        Point p = points[0], q = points[points.length - 1];
        int i = points.length - 2;
        while (i >= 0 && ccw(p, q, points[i]) == 0)
            i--;    
        // reverse sort order of collinear points in the end positions
        for (int l = i + 1, h = points.length - 1; l < h; l++, h--) {
            Point tmp = points[l];
            points[l] = points[h];
            points[h] = tmp;
        }
    }
}
"""

import math

# Definition for a point.
class Point(object):
  def __init__(self, a=0, b=0):
    self.x = a
    self.y = b

class Solution(object):
  def outerTrees(self, points):
    """
    :type points: List[Point]
    :rtype: List[Point]
    """
    # step 0: Corner case
    n = len(points)
    if n <= 3: return points

    output = []
    # step 1: find a point definitely on the convex hull
    first_index = 0
    x_min, y_min = points[0].x, points[0].y
    for i in range(1,len(points)):
      if points[i].x < x_min or (points[i].x==x_min and points[i].y<y_min):
        x_min, y_min = points[i].x, points[i].y
        first_index = i
    output.append(points[first_index])

    # step 2: clockwise
    cnt = 0
    curr_index = first_index
    while(True):
      curr = output[-1]
      first = points[0] 
      # go through all points,
      new_index = 0 
      for i in range(1, len(points)):
        if i != curr_index:
          cross = self.cross_product(first, curr, points[i])
          if new_index==curr_index or cross < 0 or (cross==0 and self.distance(points[i], curr)>self.distance(first, curr)):
            first = points[i]
            new_index = i
      # colinear-case
      for i in range(len(points)):
        # add points on line curr, first
        if i!=curr_index and i!=new_index:
          cross = self.cross_product(first, curr, points[i])
          if cross == 0:
            output.append(points[i])
      curr_index = new_index
      if curr_index == first_index:
        break
      cnt += 1
      if cnt == 10: break
      output.append(first)
    return output

  def distance(self, pt1, pt2):
    return (pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2  

  def cross_product(self, pt1, pt2, pt3):
    x12 = pt1.x - pt2.x
    x13 = pt1.x - pt3.x
    y12 = pt1.y - pt2.y
    y13 = pt1.y - pt3.y
    return -x12*y13+x13*y12

  def solution2(self, points):
    def sign(p, q, r):
        return cmp((p.x - r.x)*(q.y - r.y), (p.y - r.y)*(q.x - r.x))
    
    def drive(hull, r):
        hull.append(r)
        while len(hull) >= 3 and sign(*hull[-3:]) < 0:
            hull.pop(-2)
        return hull
    
    points.sort(key = lambda p: (p.x, p.y))
    lower = reduce(drive, points, [])
    upper = reduce(drive, points[::-1], [])
    return list(set(lower + upper))

def print_pts(points):
  for item in points:
    print item.x, item.y

if __name__ == '__main__':
  # pts_list = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
  # pts_list = [[3,7],[6,8],[7,8],[11,10],[4,3],[8,5],[7,13],[4,13]]
  # pts_list = [[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]
  # pts_list = [[0,2],[1,1],[2,2],[2,4],[4,2],[3,3]]
  pts_list = [[0,0],[0,1],[0,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0]]
  points = []
  for i,j in pts_list:
    points.append(Point(i, j))
  a = Solution()
  result = a.outerTrees(points)
  print 'result1'
  print_pts(result)
  result2 = a.solution2(points)
  print 'result2'
  print_pts(result2)

