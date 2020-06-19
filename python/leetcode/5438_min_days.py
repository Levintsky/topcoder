class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)
        if n < m * k:
            return -1
        vs = list(set([item for item in bloomDay]))
        vs.sort()
        l, r = 0, len(vs)-1
        best = vs[-1]
        
        def check_valid(v, k, m):
            arr = [0]
            for item in bloomDay:
                if item <= v:
                    arr[-1] += 1
                else:
                    if arr[-1] > 0:
                        arr.append(0)
            res = 0
            for item in arr:
                res += item // k
            return res >= m
        
        while l <= r:
            mid = (l + r) // 2
            item = vs[mid]
            # check doable
            if check_valid(item, k, m):
                best = min(best, item)
                r = mid - 1
            else:
                l = mid + 1
        return best


if __name__ == "__main__":
    a = Solution()
    print(a.minDays([7,7,7,7,12,7,7], 2, 3))