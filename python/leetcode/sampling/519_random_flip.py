"""
519. Random Flip Matrix (Medium)

You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix where all values are initially 0. Write a function flip which chooses a 0 value uniformly at random, changes it to 1, and then returns the position [row.id, col.id] of that value. Also, write a function reset which sets all values back to 0. Try to minimize the number of calls to system's Math.random() and optimize the time and space complexity.

Note:

1 <= n_rows, n_cols <= 10000
0 <= row.id < n_rows and 0 <= col.id < n_cols
flip will not be called when the matrix has no 0 values left.
the total number of calls to flip and reset will not exceed 1000.
Example 1:

Input:
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
Output: [null,[0,1],[1,2],[1,0],[1,1]]
Example 2:

Input:
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]
Output: [null,[0,0],[0,1],null,[0,0]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, n_rows and n_cols. flip and reset have no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""

"""
Best explanation!!
We will be using modern method of the Fisher–Yates shuffle.

Please read how the original algorithm works first: Examples

So, the steps are:

generate random from 0 to n : m
swap m and n
decrease n
"""

"""
O(1) random
O(k) space (time of flip)
flip generally << m * n

Similar idea with some explanation:
Here we are modeling the matrix as a 1d array with initial size of row*cols.
For each flip, randomly pick an index from 0 to size-1 and flip it.
int r = rand.nextInt(total--);
Then swap that flipped element with the tail element (index: size-1), store that mapping info (key: origin index, value: index of the tail) into a Map and decrease the size.
map.put(r, map.getOrDefault(total, total));
Next time when we randomly pick a same index we can go to the map and find the actual element stores in that index
int x = map.getOrDefault(r, r);

class Solution {

    Map<Integer, Integer> map;
    int rows, cols, total;
    Random rand;
    
    public Solution(int n_rows, int n_cols) {
        map = new HashMap<>();
        rand = new Random();
        rows = n_rows; 
        cols = n_cols; 
        total = rows * cols;
    }
    
    public int[] flip() {
        int r = rand.nextInt(total--);
        int x = map.getOrDefault(r, r);
        map.put(r, map.getOrDefault(total, total));
        return new int[]{x / cols, x % cols};
    }
    
    public void reset() {
        map.clear();
        total = rows * cols;
    }
}
"""

import random

class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.memo = {}
        for i in range(n_rows * n_cols):
            self.memo[i] = i
        self.size = n_rows * n_cols

    def flip(self) -> List[int]:
        n = random.randint(0, self.size-1)
        self.size -= 1
        if self.memo[n] == n:
            self.memo[n] = self.size
            i, j = n // self.n_cols, n % self.n_cols
        else:
            k = self.memo[n]
            self.memo[n] = self.size
            i, j = k // self.n_cols, k % self.n_cols
        return [i, j]

    def reset(self) -> None:
        for i in range(n_rows * n_cols):
            self.memo[i] = i
        self.size = n_rows * n_cols


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
