"""
1504. Count Submatrices With All Ones (Medium)

Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

 

Example 1:

Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:

Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
Example 3:

Input: mat = [[1,1,1,1,1,1]]
Output: 21
Example 4:

Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5
 

Constraints:

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
"""


class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        height = [0] * n
        res = 0
        for row in mat:
            # update height
            for i in range(n):
                if row[i] == 1:
                    height[i] += 1
                else:
                    height[i] = 0
            # print('before', height)
            # handle height

            tmpres = [0] * n
            for j in range(n):
                curr = height[j]
                k = j
                while k >= 0:
                    tmpres[j] += curr
                    k -= 1
                    curr = min(curr, height[k])
                    if curr == 0:
                        break
            print(tmpres)
            res += sum(tmpres)

            """
            j = n-1
            height_copy = [item for item in height]
            while j >= 0:
                if j != n-1 and height_copy[j+1] != 0:
                    res += max(height_copy[j]-height_copy[j+1], 0)
                    height_copy[j] = min(height_copy[j], height_copy[j+1])
                j -= 1
            print('after', height_copy)
            # presum
            presum = [0]
            for item in height_copy:
                if item == 0:
                    presum.append(0)
                else:
                    presum.append(presum[-1]+item)
            print('presum', presum[::-1])
            # print(presum)

            res += sum(presum)
            """
        return res

if __name__ == "__main__":
    a = Solution()
    print(a.numSubmat([[1,0,1],
              [1,1,0],
              [1,1,0]]))
    print(a.numSubmat([[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]))
    print(a.numSubmat([[1,1,1,1,1,1]]))
    print(a.numSubmat([[1,0,1],[0,1,0],[1,0,1]]))
    arr = [[1,1,1,1,0,1,0],[1,1,1,0,0,0,1],[0,1,1,1,1,0,0],[1,1,0,1,1,0,1],[1,0,0,0,0,0,1],[1,1,0,1,1,1,1],[1,1,0,0,1,1,1]]
    print(a.numSubmat(arr))