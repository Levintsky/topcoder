"""
1163. Last Substring in Lexicographical Order (Hard)

Given a string s, return the last substring of s in lexicographical order.

Example 1:

Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
Example 2:

Input: "leetcode"
Output: "tcode"
 

Note:

1 <= s.length <= 10^5
s contains only lowercase English letters.

"""

class Node(object):
    """A node in the suffix tree. 
    
    suffix_node
        the index of a node with a matching suffix, representing a suffix link.
        -1 indicates this node has no suffix link.
    """
    def __init__(self):
        self.suffix_node = -1   

    def __repr__(self):
        return "Node(suffix link: %d)"%self.suffix_node

class Edge(object):
    """An edge in the suffix tree.
    
    first_char_index
        index of start of string part represented by this edge
        
    last_char_index
        index of end of string part represented by this edge
        
    source_node_index
        index of source node of edge
    
    dest_node_index
        index of destination node of edge
    """
    def __init__(self, first_char_index, last_char_index, source_node_index, dest_node_index):
        self.first_char_index = first_char_index
        self.last_char_index = last_char_index
        self.source_node_index = source_node_index
        self.dest_node_index = dest_node_index
        
    @property
    def length(self):
        return self.last_char_index - self.first_char_index

    def __repr__(self):
        return 'Edge(%d, %d, %d, %d)'% (self.source_node_index, self.dest_node_index 
                                        ,self.first_char_index, self.last_char_index )


class Suffix(object):
    """Represents a suffix from first_char_index to last_char_index.
    
    source_node_index
        index of node where this suffix starts
    
    first_char_index
        index of start of suffix in string
        
    last_char_index
        index of end of suffix in string
    """
    def __init__(self, source_node_index, first_char_index, last_char_index):
        self.source_node_index = source_node_index
        self.first_char_index = first_char_index
        self.last_char_index = last_char_index
        
    @property
    def length(self):
        return self.last_char_index - self.first_char_index
                
    def explicit(self):
        """A suffix is explicit if it ends on a node. first_char_index
        is set greater than last_char_index to indicate this.
        """
        return self.first_char_index > self.last_char_index
    
    def implicit(self):
        return self.last_char_index >= self.first_char_index

        
class SuffixTree(object):
    """A suffix tree for string matching. Uses Ukkonen's algorithm
    for construction.
    """
    def __init__(self, string, case_insensitive=False):
        """
        string
            the string for which to construct a suffix tree
        """
        self.string = string
        self.case_insensitive = case_insensitive
        self.N = len(string) - 1
        self.nodes = [Node()]
        self.edges = {}
        self.active = Suffix(0, 0, -1)
        if self.case_insensitive:
            self.string = self.string.lower()
        for i in range(len(string)):
            self._add_prefix(i)
    
    def __repr__(self):
        """ 
        Lists edges in the suffix tree
        """
        curr_index = self.N
        s = "\tStart \tEnd \tSuf \tFirst \tLast \tString\n"
        values = list(self.edges.values())
        values.sort(key=lambda x: x.source_node_index)
        for edge in values:
            if edge.source_node_index == -1:
                continue
            s += "\t%s \t%s \t%s \t%s \t%s \t"%(edge.source_node_index
                    ,edge.dest_node_index 
                    ,self.nodes[edge.dest_node_index].suffix_node 
                    ,edge.first_char_index
                    ,edge.last_char_index)
                    
            
            top = min(curr_index, edge.last_char_index)
            s += self.string[edge.first_char_index:top+1] + "\n"
        return s
            
    def _add_prefix(self, last_char_index):
        """The core construction method.
        """
        last_parent_node = -1
        while True:
            parent_node = self.active.source_node_index
            if self.active.explicit():
                if (self.active.source_node_index, self.string[last_char_index]) in self.edges:
                    # prefix is already in tree
                    break
            else:
                e = self.edges[self.active.source_node_index, self.string[self.active.first_char_index]]
                if self.string[e.first_char_index + self.active.length + 1] == self.string[last_char_index]:
                    # prefix is already in tree
                    break
                parent_node = self._split_edge(e, self.active)
        

            self.nodes.append(Node())
            e = Edge(last_char_index, self.N, parent_node, len(self.nodes) - 1)
            self._insert_edge(e)
            
            if last_parent_node > 0:
                self.nodes[last_parent_node].suffix_node = parent_node
            last_parent_node = parent_node
            
            if self.active.source_node_index == 0:
                self.active.first_char_index += 1
            else:
                self.active.source_node_index = self.nodes[self.active.source_node_index].suffix_node
            self._canonize_suffix(self.active)
        if last_parent_node > 0:
            self.nodes[last_parent_node].suffix_node = parent_node
        self.active.last_char_index += 1
        self._canonize_suffix(self.active)
        
    def _insert_edge(self, edge):
        self.edges[(edge.source_node_index, self.string[edge.first_char_index])] = edge
        
    def _remove_edge(self, edge):
        self.edges.pop((edge.source_node_index, self.string[edge.first_char_index]))
        
    def _split_edge(self, edge, suffix):
        self.nodes.append(Node())
        e = Edge(edge.first_char_index, edge.first_char_index + suffix.length, suffix.source_node_index, len(self.nodes) - 1)
        self._remove_edge(edge)
        self._insert_edge(e)
        self.nodes[e.dest_node_index].suffix_node = suffix.source_node_index  ### need to add node for each edge
        edge.first_char_index += suffix.length + 1
        edge.source_node_index = e.dest_node_index
        self._insert_edge(edge)
        return e.dest_node_index

    def _canonize_suffix(self, suffix):
        """This canonizes the suffix, walking along its suffix string until it 
        is explicit or there are no more matched nodes.
        """
        if not suffix.explicit():
            e = self.edges[suffix.source_node_index, self.string[suffix.first_char_index]]
            if e.length <= suffix.length:
                suffix.first_char_index += e.length + 1
                suffix.source_node_index = e.dest_node_index
                self._canonize_suffix(suffix)
 

    # Public methods
    def find_substring(self, substring):
        """Returns the index of substring in string or -1 if it
        is not found.
        """
        if not substring:
            return -1
        if self.case_insensitive:
            substring = substring.lower()
        curr_node = 0
        i = 0
        while i < len(substring):
            edge = self.edges.get((curr_node, substring[i]))
            if not edge:
                return -1
            ln = min(edge.length + 1, len(substring) - i)
            if substring[i:i + ln] != self.string[edge.first_char_index:edge.first_char_index + ln]:
                return -1
            i += edge.length + 1
            curr_node = edge.dest_node_index
        return edge.first_char_index - len(substring) + ln
        
    def has_substring(self, substring):
        return self.find_substring(substring) != -1


class TrieNode(object):
    def __init__(self):
        self.child = [None] * 26
        self.is_word = False

class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        root = TrieNode()

        n = len(s)
        if n == 0: return ""

        maxc = s[0]
        for c in s:
            maxc = max(c, maxc)

        for i in range(n):
            if s[i] != maxc:
                continue
            subs = s[i:]
            # add subs to the tree
            node = root
            for j, c in enumerate(subs):
                ind = ord(c) - ord('a')
                if not node.child[ind]:
                    node.child[ind] = TrieNode()
                node = node.child[ind]
                if j == len(subs) - 1:
                    node.is_word = True

        res = ""
        node = root
        while True:
            flag = False
            for j in range(25, -1, -1):
                if node.child[j] is not None:
                    res += chr(ord('a') + j)
                    flag = True
                    node = node.child[j]
                    break
            if not flag:
                break
        return res

    def solve2(self, s):
        n = len(s)
        if n == 0:
            return ""
        visited = [False] * n
        memo = []
        for i in range(26):
            memo.append([])
        for i, c in enumerate(s):
            ind = ord(c) - ord('a')
            memo[ind].append(i)

        def set_val(indices, val):
            for i in indices:
                visited[i] = val
            return
        # go back from z
        candidates = []
        for i in range(25, -1, -1):
            if len(memo[i]) > 0:
                candidates = [item for item in memo[i]]
                set_val(candidates, True)
                break
        offset = 1
        while len(candidates) > 1:
            # get there next
            # next_cand = [item + offset for item in candidates if item + offset < n]
            chars = [s[item + offset] for item in candidates if item + offset < n]
            max_char = max(chars)
            new_cand = []
            to_remove = set()
            for ind in candidates:
                if ind + offset >= n:
                    continue
                # if == max_char, then 
                if s[ind + offset] == max_char:
                    if visited[ind + offset]:
                        to_remove.add(ind + offset)
                    if ind not in to_remove:
                        new_cand.append(ind)
                visited[ind + offset] = True
            offset += 1
            candidates = new_cand
        return s[candidates[0]:]


if __name__ == "__main__":
    a = Solution()
    print(a.solve2("abab"))
    print(a.solve2("leetcode"))


"""
First, the answer must be starting with the largest letter, ending at the end of string S. So we save all the "candidates" by their starting point, and assign a pointer to each of them (pointing at the start).
Then we increment the pointer for each candidate, using following rules:

We filter the candidates by the letter their pointers are at. Only the ones with the largest letter will go into next round.
If a pointer meets a starting point, it "swallows" the next candidate like a snake.
In the following image, pointer of A meets the starting point of B. Suppose we want to keep candidate B. The only possibility is the future letters are lexicographically larger than candidate B, so appending it to B makes B larger than A. Apprently it can not be, otherwise B (and A) will not be selected initially as candidates.

Finally we will have only one candidate.
This gives O(n) time complexity. Not very strictly, assume we start with k candidates, then eliminating all except one candidate takes n/k steps. In each step, we only increment the pointer of each candidate by one.
Correct me if I made a mistake. :)

class Solution:
    def lastSubstring(self, s: str) -> str:
        count=collections.defaultdict(list)
        for i in range(len(s)):
            count[s[i]].append(i)
        largeC=max(count.keys())
        starts={}
        for pos in count[largeC]:
            starts[pos]=pos+1
        # Initialize all candidates and their pointers
        
        while len(starts)>1:
        # Eliminate till we have only one
            toDel=set()
            nextC=collections.defaultdict(list)
            for start,end in starts.items():
                if end==len(s):
                # Remove if reaching the end
                    toDel.add(start)
                    continue
                    
                nextC[s[end]].append(start)
                # Filter by current letter
                
                if end in starts:
                    toDel.add(end)
                # "Swallow" the latter candidate
            
            nextStarts={}
            largeC=max(nextC.keys())
            for start in nextC[largeC]:
                if start not in toDel:
                    nextStarts[start]=starts[start]+1
                    # Select what we keep for the next step
            starts=nextStarts.copy()
        for start,end in starts.items():
            return s[start:]
"""