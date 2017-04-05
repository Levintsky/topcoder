'''
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N-h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
'''

class Solution(object):
  def hIndex(self, citations):
    n = len(citations)
    if n == 0:
      return 0
    # bucket sort
    bucket = {}
    for item in citations:
      item = min(item, n)
      if item in bucket:
        bucket[item] += 1
      else:
        bucket[item] = 1
    # statistics
    i = n
    h_index = 0
    curr_paper = 0
    min_cite = 0
    while(i>=0):
      if i in bucket:
        curr_paper += bucket[i]
        min_cite = i
        h_index = max(h_index, min(min_cite, curr_paper))
      i -= 1
    return h_index


if __name__ == '__main__':
  a = Solution()
  print a.hIndex([3,0,6,1,5])
