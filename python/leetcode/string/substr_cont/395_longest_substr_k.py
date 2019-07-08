"""
395. Longest Substring with At Least K Repeating Characters (Medium)

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

"""
As pointed out by @hayleyhu, I can just take the first too rare character instead of a rarest. Submitted once, accepted in 48 ms.

def longestSubstring(self, s, k):
    for c in set(s):
        if s.count(c) < k:
            return max(self.longestSubstring(t, k) for t in s.split(c))
    return len(s)

If every character appears at least k times, the whole string is ok. Otherwise split by a least frequent character (because it will always be too infrequent and thus can't be part of any ok substring) and make the most out of the splits.

As usual for Python here, the runtime varies a lot, this got accepted in times from 32 ms to 74 ms.
"""
import collections

class Solution(object):
  def longestSubstring(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    stat = dict(collections.Counter(s))
    result = 0
    if min(stat.values()) >= k:
      return len(s)
    if max(stat.values()) < k:
      return 0
    # divide and conquer
    start_id = -1
    substr = ''

    split_set = []
    for key in stat.keys():
      if stat[key] < k:
        split_set.append(key)
    split_list = [s]
    new_list = []
    for c in split_set:
      # char
      for item in split_list:
        tmp = item.split(c)
        for item2 in tmp: 
          if len(item2)>=k: new_list.append(item2)
      new_list, split_list = [], new_list
    
    max_ = 0
    for item in split_list:
      max_ = max(max_, self.longestSubstring(item, k))
    return max_ 

if __name__ == '__main__':
  a = Solution()
  print a.longestSubstring('aaabb', 3)
  print a.longestSubstring('ababb', 2)
  print a.longestSubstring("ababacb", 3)
