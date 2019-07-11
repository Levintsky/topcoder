"""
799. Champagne Tower (Medium)

We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup (250ml) of champagne.

Then, some champagne is poured in the first glass at the top.  When the top most glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has it's excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

Now after pouring some non-negative integer cups of champagne, return how full the j-th glass in the i-th row is (both i and j are 0 indexed.)

Example 1:
Input: poured = 1, query_glass = 1, query_row = 1
Output: 0.0
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:
Input: poured = 2, query_glass = 1, query_row = 1
Output: 0.5
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
 

Note:

poured will be in the range of [0, 10 ^ 9].
query_glass and query_row will be in the range of [0, 99].
"""

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        if poured == 0:
            return 0
        state = {(0,0): 1., (1,0): 0., (1,1): 0.}
        active = set([(0,0)]) # full but active
        notfull = set([(1,0), (1,1)]) # to get filled
        for i in range(poured-1):
            tmp_memo = {}
            total = 0
            for x, y in notfull:
                par = x-1, y-1
                if par in active:
                    tmp_memo[(x,y)] = tmp_memo.get((x,y), 0) + 1
                    total += 1
                par = x-1, y
                if par in active:
                    tmp_memo[(x,y)] = tmp_memo.get((x,y), 0) + 1
                    total += 1
            # update
            for x, y in notfull:
                state[(x,y)] = state.get((x,y), 0.) + tmp_memo[(x,y)] / total
            # update notfull
            to_active = []
            new_notfull = []
            for x, y in notfull:
                if state[(x,y)] > 0.999:
                    to_active.append((x,y))
                    if x+1 < 100:
                        new_notfull.append((x+1, y))
                        new_notfull.append((x+1, y+1))
            for item in to_active:
                notfull.remove(item)
                active.add(item)
            for item in new_notfull:
                notfull.add(item)
            # update active: remove non-active
            to_remove = []
            for x, y in active:
                if state.get((x+1,y), 0) > 0.999 and state.get((x+1, y+1), 0) > 0.999:
                    to_remove.append((x,y))
            for item in to_remove:
                active.remove(item)
            
            if state.get((query_row, query_glass), 0) > 0.999:
                return 1.
            print(state)

    def solve2(self, poured, query_row, query_glass):
        ref = [[1.]]
        curr = [[0.]]
        for i in range(99):
            curr.append([0.] * (i+2))
            old_ref = ref[-1]
            new_ref = [0.] * (i+2)
            new_ref[0] = 1 / (2 ** (i+1))
            new_ref[-1] = 1 / (2 ** (i+1))
            for j, item in enumerate(old_ref):
                if j != len(old_ref) - 1:
                    new_ref[j+1] = (old_ref[j] + old_ref[j+1]) / 2.
            ref.append(new_ref)
        if poured != 0:
            curr[0][0] = 1.
            poured -= 1
        else:
            return 0.

        if query_row == 0:
            return 1.

        # active
        q_i, q_j = query_row, query_glass
        active = set([(1, 0), (1, 1)])
        for p in range(poured):
            to_remove = []
            to_add = []
            for i, j in active:
                if j > 0 and curr[i-1][j-1] > .999 and (i-1, j-1) not in active:
                    curr[i][j] += ref[i-1][j-1] / 2.
                if j < len(curr[i-1]) and curr[i-1][j] > .999 and (i-1, j) not in active:
                    curr[i][j] += ref[i-1][j] / 2.
                if curr[i][j] >= 1.:
                    to_remove.append((i, j))
                    diff = curr[i][j] - 1.
                    curr[i+1][j] += diff / 2.
                    curr[i+1][j+1] += diff / 2.
                    curr[i][j] = 1.
                    if i+1 < 100:
                        to_add.append((i+1,j))
                        to_add.append((i+1,j+1))
            for item in to_remove:
                active.remove(item)
            for item in to_add:
                active.add(item)
            if curr[q_i][q_j] > .999:
                return 1.
            # check parent full
            if q_j == 0 and curr[q_i-1][0] > .999:
                return min(1., curr[q_i][0] + (poured-p-1) * ref[q_i][0]) / 2.
            elif q_j == q_i and curr[q_i-1][q_j-1] > .999:
                return min(1., curr[q_i][-1] + (poured-p-1) * ref[q_i][-1]) / 2.
            elif curr[q_i-1][q_j-1] > .999 and curr[q_i-1][q_j] > .999:
                return min(1., curr[q_i][q_j] + (poured-p-1) * (ref[q_i-1][q_j-1] + ref[q_i-1][q_j]) / 2. )
            print(curr[:5])
        return curr[q_i][q_j]

    def solve3(self, poured, query_row, query_glass):
        ref = []
        for i in range(1, 101):
            ref.append([0.] * i)
        ref[0][0] = poured
        for i in range(min(99, query_row)):
            flag = False
            for j in range(i+1):
                if ref[i][j] > 1:
                    diff = ref[i][j] - 1.
                    ref[i][j] = 1.
                    ref[i+1][j] += diff / 2.
                    ref[i+1][j+1] += diff / 2.
                    flag = True
            if not flag:
                break
        return min(ref[query_row][query_glass], 1.)


if __name__ == "__main__":
    a = Solution()
    # print(a.champagneTower(20, 10,8))
    print(a.solve3(7, 3, 1))
