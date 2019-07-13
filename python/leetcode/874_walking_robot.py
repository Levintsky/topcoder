import bisect

class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        memo_y2x = {}
        memo_x2y = {}
        for x, y in obstacles:
            if y not in memo_y2x:
                memo_y2x[y] = []
            if x not in memo_x2y:
                memo_x2y[x] = []
            memo_y2x[y].append(x)
            memo_x2y[x].append(y)
        # sort for further binary sort
        for k in memo_x2y.keys():
            memo_x2y[k].sort()
        for k in memo_y2x.keys():
            memo_y2x[k].sort()
        # bisect
        curr_dir = 0 # (0, 1, 2, 3) for up, right, down, left
        curr_pos = [0, 0] # x, y
        for c in commands:
            if c == -1:
                curr_dir = (curr_dir + 1) % 4
            elif c == -2:
                curr_dir = (curr_dir - 1) % 4
            else:
                x, y = curr_pos
                # up
                if curr_dir == 0:
                    if x in memo_x2y:
                        yind = bisect.bisect(memo_x2y[x], y)
                        if yind == len(memo_x2y[x]):
                            y += c
                        else:
                            y = min(y+c, memo_x2y[x][yind]-1)
                    else:
                        y += c
                elif curr_dir == 1: # right
                    if y in memo_y2x:
                        xind = bisect.bisect(memo_y2x[y], x)
                        if xind == len(memo_y2x[y]):
                            x += c
                        else:
                            x = min(x+c, memo_y2x[y][xind]-1)
                    else:
                        x += c
                elif curr_dir == 2: # down
                    if x in memo_x2y:
                        yind = bisect.bisect(memo_x2y[x], y) - 1
                        if yind == -1:
                            y -= c
                        else:
                            y = max(y-c, memo_x2y[x][yind]+1)
                    else:
                        y -= c
                else: # left
                    if y in memo_y2x:
                        xind = bisect.bisect(memo_y2x[y], x) - 1
                        if xind == -1:
                            x -= c
                        else:
                            x = max(x-c, memo_y2x[y][xind]+1)
                    else:
                        x -= c

                curr_pos = [x, y]
            # print(curr_pos, curr_dir)
        # print(curr_pos)
        res = sum([item**2 for item in curr_pos])
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.robotSim([4,-1,3], []))
    print(a.robotSim([-2, -2, 4,-1,4,-2,4], [[-2,-4]]))
