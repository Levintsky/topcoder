import math


class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        n = len(positions)
        if n == 1:
            return 0.
        curr = [0., 0.]
        for x, y in positions:
            curr[0] += x
            curr[1] += y
        curr = [item / n for item in curr]

        def get_diff(positions, curr):
            diff = [[pos[0]-curr[0], pos[1]-curr[1]] for pos in positions]
            return diff

        def get_dist(diff, eps=1.e-10):
            dist = [d[0] ** 2 + d[1] ** 2 for d in diff]
            dist = [math.sqrt(item) + eps for item in dist]
            return dist

        def get_grad(diff, dist):
            grad = [[dif[0]/dis, dif[1]/dis] for dif, dis in zip(diff, dist)]
            grad = [sum([item[0] for item in grad]) / n, sum([item[1] for item in grad]) / n]
            return grad

        last_dist = 1000000.
        # iter_ = 1.
        while True:
        # for i in range(100):
            # get diff
            diff = get_diff(positions, curr)

            # get dist
            dist = get_dist(diff)

            # get grad
            grad = get_grad(diff, dist)

            curr = [curr[0] + grad[0]/2., curr[1] + grad[1]/2.]
            # iter_ += 1.

            real_dist = get_dist(diff, 0.)
            dist_sum = sum(real_dist)
            print(curr, dist_sum)

            if last_dist - dist_sum < 1.e-8:
                break
            else:
                last_dist = dist_sum

        # dist = get_dist(diff, 0.)
        return dist_sum


if __name__ == "__main__":
    a = Solution()
    """
    print(a.getMinDistSum([[0,1],[1,0],[1,2],[2,1]]))
    print(a.getMinDistSum([[1,1],[3,3]]))
    print(a.getMinDistSum([[1,1]]))
    print(a.getMinDistSum([[1,1], [1,1]]))
    print(a.getMinDistSum([[1,1],[0,0],[2,0]]))
    print(a.getMinDistSum([[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]))
    print(a.getMinDistSum([[9,9],[31,1],[28,61],[14,42],[95,98],[37,69]]))
    """
    print(a.getMinDistSum([[44,23],[18,45],[6,73],[0,76],[10,50],[30,7],[92,59],[44,59],[79,45],[69,37],[66,63],[10,78],[88,80],[44,87]]))
