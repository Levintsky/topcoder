class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        # step 1: group groups
        memo_id2group = {}
        memo_group2ids = {}
        single = []
        for item, g in group:
        	if g == -1:
        		single.append(item)
        	else:
        		memo_id2group[item] = g
        		if g not in memo_group2ids:
        		    memo_group2ids[g] = []
        		memo_group2ids[g].append(item)
        
