class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        memo = {}
        for i, j in edges:
            if i not in memo:
                memo[i] = []
            memo[i].append(j)
        self.result = 0
        print(memo)
        
        def parse(node):
            # given: node id
            # return: True/False, n
            if node not in memo: # leaf node
                if hasApple[node]:
                    return True, 2
                else:
                    return False, 0
            flag = hasApple[node]
            result = 0
            for child in memo[node]:
                f, r = parse(child)
                if f:
                    flag = True
                    result += r
            print(node, flag, result)
            if node == 0:
                return True, result
            if flag and result == 0: # special case only self
                return True, 2
            if flag:
                return True, result + 2
            else:
                return False, 0
        
        _, self.result = parse(0)
        return self.result


if __name__ == "__main__":
    a = Solution()
    print(a.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]))
    print(a.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]))
    print(a.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,False,False,False,False,False]))
    print(a.minTime(4, [[0,1],[1,2],[0,3]], [True,True,True,True]))