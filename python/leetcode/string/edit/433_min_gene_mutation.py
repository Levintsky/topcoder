'''
433. Minimum Genetic Mutation (Medium)

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.

Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
'''

class Solution(object):
  def minMutation(self, start, end, bank):
    """
    :type start: str
    :type end: str
    :type bank: List[str]
    :rtype: int
    """
    bank = set(bank)
    visited = {0:[start]}
    if end not in bank: return -1
    curr_step = 0
    while len(bank) > 0:
      curr_step += 1
      visited[curr_step] = []
      to_remove = set([])
      for item1 in bank:
        for item2 in visited[curr_step-1]:
          if self.dist(item1, item2) == 1:
            to_remove.add(item1)
            visited[curr_step].append(item1)
            if item1 == end: return curr_step
      for item in to_remove: bank.remove(item)
      if not visited[curr_step]: return -1
      print bank
      print visited
    return -1

  def dist(self, str1, str2):
    cnt = 0
    i = 0
    while i < len(str1):
      if str1[i] != str2[i]:
        cnt += 1
      i += 1
    return cnt


if __name__ == '__main__':
  start = "AACCTTGG"
  end = "AATTCCGG"
  bank = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]

  a = Solution()
  print a.minMutation(start, end, bank)
