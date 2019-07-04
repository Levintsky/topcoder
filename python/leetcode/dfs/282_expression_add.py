'''
282. Expression Add Operators (Hard)

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
'''

class Solution(object):
  def addOperators(self, num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    l = []
    n = len(num)
    for i in range(n):
      l.append(num[i])

    # add +, -, *
    # generate all possible combinatorial
    result = []
    for i in range(4**(n-1)):
      # parse i
      l2 = []
      tmp = i
      while len(l2)!=n-1:
        if tmp % 4 == 0: l2.append('+')
        elif tmp % 4 == 1: l2.append('-')
        elif tmp % 4 == 2: l2.append('*')
        else: l2.append('')
        tmp /= 4
      # interleaving
      l3 = [0] * (2*n-1)
      l3[::2] = l
      l3[1::2] = l2
      # print l, l2, l3
      formula = ''.join(l3)
      if eval(formula) == target:
        result.append(formula)
    return result

  def solve2(self, num, target):
    self.l = []
    n = len(num)
    for i in range(n):
      self.l.append(num[i])
    self.result = []
    self.l2 = [''] * (n-1)
    self.l3 = [''] * (2*n-1)
    self.dfs(0, self.l, target)
    return self.result

  def dfs(self, i, l, target):
    n = len(self.l)
    for j in range(4):
      if j == 0: self.l2[i] = '+'
      elif j == 1: self.l2[i] = '-'
      elif j == 2: self.l2[i] = '*'
      else: self.l2[i] = ''

      if self.l2[i] == '' and l[i] == '0': continue
      if i == n-2:
        self.l3[::2] = self.l
        self.l3[1::2] = self.l2
        formula = ''.join(self.l3)
        # print formula
        if eval(formula) == target:
          self.result.append(formula)
      else:
        self.dfs(i+1, self.l, target)
if __name__ == "__main__":
  a = Solution()
  # print a.addOperators("123", 6)
  print a.solve2("123", 6)
  # print a.addOperators("232", 8)
  print a.solve2("232", 8)
  # print a.addOperators("105", 5)
  print a.solve2("105", 5)
  # print a.addOperators("00", 0)
  print a.solve2("00", 0)
  # print a.addOperators("34567890", 9191)
  print a.solve2("34567890", 9191)
  print a.solve2("123456789", 45)
  print a.solve2("", 5)
