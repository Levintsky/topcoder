class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = ""
        while A > 0 or B > 0:
            if A > B:
                nA, nB = min(2, A), min(1, B)
                if res == "" or res[-1] == 'b':
                    res += 'a' * nA + 'b' * nB
                else:
                	res += 'b' * nB + 'a' * nA
                A , B = A - nA, B - nB
            elif A < B:
                nA, nB = min(1, A), min(2, B)
                if res == "" or res[-1] == 'a':
                    res += 'b' * nB + 'a' * nA
                else:
                	res += 'a' * nA + 'b' * nB
                A, B = A - nA, B - nB
            else:
                if len(res) == 0 or res[-1] == 'B':
                    res += "ab" * A
                else:
                    res += "ba" * A
                A = 0
                B = 0
        return res

if __name__ == "__main__":
    a = Solution()
    print(a.strWithout3a3b(1, 2))
    print(a.strWithout3a3b(4, 1))