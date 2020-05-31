class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        memo = {}
        for i, j in edges:
            if i not in memo:
                memo[i] = []
            if j not in memo:
                memo[j] = []
            memo[i].append(j)
            memo[j].append(i)
            # i, j = min(i, j), max(i, j)
            # if i not in memo_child:
                # memo_child[i] = []
            # memo_child[i].append(j)
            # memo_parent[j] = i
        if len(memo) == 0:
            return [0] * N
            
        memo_stat = {} # node index to subtree count, dist
        def traverse(idx, par_id):
            # leaf
            if len(memo[idx]) == 1 and memo[idx][0] == par_id:
                memo_stat[idx] = 1, 0
                return 1, 0
            cnt, dist = 1, 0
            # for child_idx in memo_child[idx]:
            for child_idx in memo[idx]:
                if child_idx == par_id:
                    continue    
                tmp_cnt, tmp_dist = traverse(child_idx, idx)
                cnt += tmp_cnt
                dist += tmp_dist + tmp_cnt
            memo_stat[idx] = cnt, dist
            return cnt, dist
        
        traverse(0, -1)
        # print(memo_stat)
        result = [0] * N
        result[0] = memo_stat[0][1]
        
        def traverse2(idx, par_id):
            if par_id >= 0:
                # par_idx = memo_parent[idx]
                # par_result = result[par_idx]
                result[idx] = result[par_id] + N - 2 * memo_stat[idx][0]
            for child_idx in memo[idx]:
                if child_idx == par_id:
                    continue
                traverse2(child_idx, idx)
        traverse2(0, -1)
        
        return result
                

if __name__ == "__main__":
    a = Solution()
    print(a.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))
    print(a.sumOfDistancesInTree(3, [[2,1],[0,2]]))
