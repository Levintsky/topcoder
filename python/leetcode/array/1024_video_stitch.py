"""
1024. Video Stitching (Medium)

You are given a series of video clips from a sporting event that lasted T seconds.  These video clips can be overlapping with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].  We can cut these clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event ([0, T]).  If the task is impossible, return -1.



Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation:
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
Example 2:

Input: clips = [[0,1],[1,2]], T = 5
Output: -1
Explanation:
We can't cover [0,5] with only [0,1] and [0,2].
Example 3:

Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
Output: 3
Explanation:
We can take clips [0,4], [4,7], and [6,9].
Example 4:

Input: clips = [[0,4],[2,8]], T = 5
Output: 2
Explanation:
Notice you can have extra video after the event ends.


Note:

1 <= clips.length <= 100
0 <= clips[i][0], clips[i][1] <= 100
0 <= T <= 100
"""


class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        nclips = len(clips)
        if nclips == 0 and T > 0:
            return False
        if nclips == 0 and T == 0:
            return nclips
        if T == 0:
            return 0
        clips.sort(key=lambda item: (item[0], -item[1]))
        result = []
        result.append([clips[0][0], clips[0][1], 0])
        if clips[0][0] > 0:
            return -1
        if clips[0][1] >= T:
            return 1

        for i in range(1, nclips):
            if clips[i][1] <= result[-1][1]:
                continue
            if clips[i][0] > result[-1][1]:
                return -1
            # evict un-necessary
            if clips[i][1] > result[-1][2]:
                while result[-1][-1] >= clips[i][0]:
                    _ = result.pop()
                result.append([clips[i][0], clips[i][1], result[-1][1]])
            print(result)
            if result[-1][1] >= T:
                return len(result)
        return -1


if __name__ == "__main__":
    a = Solution()
    print(a.videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
    print(a.videoStitching([[0, 1], [1, 2]], 5))
    print(
        a.videoStitching(
            [
                [0, 1],
                [6, 8],
                [0, 2],
                [5, 6],
                [0, 4],
                [0, 3],
                [6, 7],
                [1, 3],
                [4, 7],
                [1, 4],
                [2, 5],
                [2, 6],
                [3, 4],
                [4, 5],
                [5, 7],
                [6, 9],
            ],
            9,
        )
    )
    print(
        a.videoStitching(
            [[5, 7], [1, 8], [0, 0], [2, 3], [4, 5], [0, 6], [5, 10], [7, 10]], 5
        )
    )
