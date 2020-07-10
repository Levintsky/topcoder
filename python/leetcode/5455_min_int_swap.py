import collections

class Solution(object):
    def minInteger(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        arr = []
        for _ in range(10):
            q = collections.deque()
            arr.append(q)
        for i, c in enumerate(num):
            n = eval(c)
            arr[n].append(i)

        # greedy
        n = len(num)
        for i in range(n):
            # work on num[i]
            tmpnum = eval(num[i])
            for j in range(tmpnum):
                pass

    def solve(self, num, k):
        num = [*map(int, num)]
        if k >= (len(num) ** 2) // 2:
            return ''.join(map(str, sorted(num)))
        
        res = []
        q = [(v, i) for i, v in enumerate(num)]
        while k and q:
            idx, (v, i) = min(enumerate(q[:k + 1]), key=lambda p:p[1])
            k -= idx
            del q[idx]
            res += v,
            
        res += [v for v, _ in q]
        return ''.join(map(str, res))


if __name__ == "__main__":
    a = Solution()
    print(a.solve("4321", 4))
