'''
394. Decode String (Medium)

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

class Solution(object):
  def decodeString(self, s):
    """
    :type s: str
    :rtype: str
    """
    char_set = set()
    for i in range(ord('a'), ord('z')+1):
      char_set.add(chr(i))

    digit_set = set()
    for i in range(ord('0'), ord('9')+1):
      digit_set.add(chr(i))
    # split to a list
    tackle_list = []
    n = len(s)
    i = 0
    tmp = ''
    while(i<n):
      if s[i] in char_set:
        tmp += s[i]
        i += 1
        if i==n or s[i] in digit_set:
          tackle_list.append(tmp)
          tmp = ''
      else: # number and [
        stat = 0
        j = i
        while(s[j] != '['): j+=1
        stat = 1
        j = j+1
        while(stat!=0):
          if s[j] == '[': stat+=1
          elif s[j] == ']': stat-=1
          j += 1
        tackle_list.append(s[i:j])
        i = j
    print tackle_list
    # generate result recursively
    result = ''
    for item in tackle_list:
      if '[' not in item:
        result += item
      else:
        i = 0
        while(item[i] !='['): i+=1
        times = int(item[:i])
        print 'working on sub-problem:', item[i+1:-1]
        subs = self.decodeString(item[i+1:-1])
        result += subs*times
    return result

  def solution2(self, s):
    # AC, faster, better solution
    result, _ = self.helper(s, 0)
    return result

  def helper(self, s, i):
    n = len(s)
    result = ''
    while i<n and s[i]!=']':
      if not self.is_digit(s[i]):
        result += s[i]
        i += 1
      else:
        # get the number first
        cnt = 0
        while(self.is_digit(s[i])):
          cnt = cnt*10 + ord(s[i])-ord('0')
          i += 1
        i += 1 # [
        tmp, i = self.helper(s, i)
        i += 1 # ]
        result += cnt * tmp
    return result, i

  def is_digit(self, c):
    if c in set(['0','1','2','3','4','5','6','7','8','9']):
      return True
    else:
      return False

if __name__ == '__main__':
  a = Solution()
  # print a.decodeString("3[a]2[bc]")
  # print a.decodeString("3[a2[c]]")
  print a.decodeString("2[abc]3[cd]ef")
  print a.solution2("2[abc]3[cd]ef")
  # print a.solution2('2[a]')
