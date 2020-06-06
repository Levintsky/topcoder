'''
385. Mini Parser (Medium)
Given a nested list of integers represented as a string, implement a parser to deserialize it.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Note: You may assume that the string is well-formed:
String is non-empty.
String does not contain white spaces.
String contains only digits '0-9' , '[' , '-' , ',' , ']'.
Example 1:
Given s = "324",
You should return a NestedInteger object which contains a single integer 324.
Example 2:
Given s = "[123,[456,[789]]]",
Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if len(s) == 0:
            return NestedInteger()
        s_split = s.split(',')
        result = self.helper(s_split)
        result_nest = self.nest_helper(result)
        return result_nest
        
                    
    def nest_helper(self, nest_arr):
        if isinstance(nest_arr, int):
            return NestedInteger(nest_arr)
        else:
            result_nest = NestedInteger()
            for item in nest_arr:
                if isinstance(item, int):
                    tmp_nest = NestedInteger(item)
                    result_nest.add(tmp_nest)
                else: # is list
                    tmp_nest = self.nest_helper(item)
                    result_nest.add(tmp_nest)
            return result_nest
                    
    def helper(self, s):
        # s: a list of str split by ','
        # return nested list of int
        n = len(s)
        # corner case
        if n == 1 and s[0][0]!='[' and s[0][-1]!=']':
            return int(s[0])
        # remove most outer []
        s[0] = s[0][1:]
        s[-1] = s[-1][:-1]
    
        result = []
        i = 0
        while(i<n):
            # if a number direct append
            if '[' not in s[i] and ']' not in s[i]:
                if len(s[i])>0:
                    result.append(int(s[i]))
                i += 1
            # else, find the group, append result
            else:
                left = s[i].count('[')
                right = s[i].count(']')
                j = i
                while(left!=right):
                    j += 1
                    left += s[j].count('[')
                    right += s[j].count(']')
                tmp_result = self.helper(s[i:j+1])
                result.append(tmp_result)
                i = j+1
        return result

if __name__ == '__main__':
  a = Solution()
  # input_ = '[1,2,3]'
  input_ = '123'# '[[1],2 ,3]'
  input_div_ = input_.split(',')
  print a.helper(input_div_)
