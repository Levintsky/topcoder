class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        eq1 = []
        eq2 = []
        for eq in equations:
            if "==" in eq:
                eq1.append(eq)
            else:
                eq2.append(eq)
        if len(eq2) == 0:
            return True
        # union-find
        res = [-1] * 26
        for eq in eq1:
            ind1 = ord(eq[0]) - ord('a')
            ind2 = ord(eq[3]) - ord('a')
            if ind1 == ind2:
                continue
            if ind1 > ind2:
                ind1, ind2 = ind2, ind1
            if res[ind1] == -1 and res[ind2] == -1:
                res[ind2] = ind1
            else:
                p1 = ind1
                while res[p1] != -1:
                    p1 = res[p1]
                p2 = ind2
                while res[p2] != -1:
                    p2 = res[p2]
                if p1 != p2: # merge parent
                    res[max(p1, p2)] = min(p1, p2)
                if ind1 != min(p1, p2):
                    res[ind1] = min(p1, p2)
                if ind2 != min(p1, p2):
                    res[ind2] = min(p1, p2)
        # check conflicts
        # print(res)
        for eq in eq2:
            ind1 = ord(eq[0]) - ord('a')
            ind2 = ord(eq[3]) - ord('a')
            while res[ind1] != -1:
                ind1 = res[ind1]
            while res[ind2] != -1:
                ind2 = res[ind2]
            if ind1 == ind2:
                return False
        return True  


if __name__ == "__main__":
    a = Solution()
    print(a.equationsPossible(["a==b","b!=a"]))
    print(a.equationsPossible(["b==a","a==b"]))
    print(a.equationsPossible(["a==b","b==c","a==c"]))
    print(a.equationsPossible(["a==b","b!=c","c==a"]))
    print(a.equationsPossible(["c==c","b==d","x!=z"]))
    print(a.equationsPossible(["f==b","c==b","c==b","e!=f"]))