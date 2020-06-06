'''
241. Different Ways to Add Parentheses (Medium)

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
'''

import re
import operator


class Solution(object):
  def helper(self, op_list):
    if len(op_list) == 1:
      return [op_list[0]]
    else:
      result = []
      for i in range(1, len(op_list)-1, 2):
        res1 = self.helper(op_list[:i])
        res2 = self.helper(op_list[i+1:])
        if op_list[i] == '+':
          res = [item1+item2 for item1 in res1 for item2 in res2]
        if op_list[i] == '-':
          res = [item1-item2 for item1 in res1 for item2 in res2]
        if op_list[i] == '*':
          res = [item1*item2 for item1 in res1 for item2 in res2]
        result += res
      return result

  def diffWaysToCompute(self, inputs):
    # first split
    neg_flag = (inputs[0] == '-')
    if neg_flag:
      inputs = inputs[1:]
    op_list = []
    i = 0
    while(i<len(inputs)):
      if inputs[i] not in ['+', '-', '*']:
        j = i
        while(j<len(inputs)):
          if j+1<len(inputs) and inputs[j+1] not in ['+','-','*']:
            j += 1
          else:
            break
        op_list.append(int(inputs[i:j+1]))
        i = j
      else:
        op_list.append(inputs[i])
      i += 1
    if neg_flag:
      op_list[0] = -op_list[0]
    print op_list
    return self.helper(op_list)

  def solve2(self, input):
   tokens = re.split('(\D)', input)
   print(tokens)
   nums = map(int, tokens[::2])
   ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
   def build(lo, hi):
       if lo == hi:
           return [nums[lo]]
       return [ops[i](a, b)
               for i in xrange(lo, hi)
               for a in build(lo, i)
               for b in build(i + 1, hi)]
   return build(0, len(nums) - 1)

if __name__ == '__main__':
  a = Solution()
  # print a.diffWaysToCompute('2-1-1')
  print(a.solve2('2-1-1'))
  print(a.solve2("2*3-4*5"))

