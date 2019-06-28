'''
301. Remove Invalid Parentheses (Hard)

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
'''

"""
Solution 1: DFS
For a better view see here

Key Points:

Generate unique answer once and only once, do not rely on Set.
Do not need preprocess.
Runtime 3 ms.
Explanation:
We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter.
The counter will increase when it is ‘(‘ and decrease when it is ‘)’. Whenever the counter is negative, we have more ‘)’ than ‘(‘ in the prefix.

To make the prefix valid, we need to remove a ‘)’. The problem is: which one? The answer is any one in the prefix. However, if we remove any one, we will generate duplicate results, for example: s = ()), we can remove s[1] or s[2] but the result is the same (). Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string. However, we need to keep another information: the last removal position. If we do not have this position, we will generate duplicate by removing two ‘)’ in two steps only with a different order.
For this, we keep tracking the last removal position and only remove ‘)’ after that.

Now one may ask. What about ‘(‘? What if s = ‘(()(()’ in which we need remove ‘(‘?
The answer is: do the same from right to left.
However a cleverer idea is: reverse the string and reuse the code!

Keypoints:
1. when stack < 0:
  i in [last_i, n-1] (because for "())())")
    j in [last_j, i] (because remove the duplicate of the same token twice)
      s[j-1] != par[1] ("))))" just remove the first one)
"""

"""
Solution 2: BFS

The idea is straightforward, with the input string s, we generate all possible states by removing one ( or ), check if they are valid, if found valid ones on the current level, put them to the final result list and we are done, otherwise, add them to a queue and carry on to the next level.

The good thing of using BFS is that we can guarantee the number of parentheses that need to be removed is minimal, also no recursion call is needed in BFS.

Thanks to @peisi, we don't need stack to check valid parentheses.

Time complexity:

In BFS we handle the states level by level, in the worst case, we need to handle all the levels, we can analyze the time complexity level by level and add them up to get the final complexity.

On the first level, there's only one string which is the input string s, let's say the length of it is n, to check whether it's valid, we need O(n) time. On the second level, we remove one ( or ) from the first level, so there are C(n, n-1) new strings, each of them has n-1 characters, and for each string, we need to check whether it's valid or not, thus the total time complexity on this level is (n-1) x C(n, n-1). Come to the third level, total time complexity is (n-2) x C(n, n-2), so on and so forth...

Finally we have this formula:

T(n) = n x C(n, n) + (n-1) x C(n, n-1) + ... + 1 x C(n, 1) = n x 2^(n-1).

Following is the Java solution:

public class Solution {
    public List<String> removeInvalidParentheses(String s) {
      List<String> res = new ArrayList<>();
      
      // sanity check
      if (s == null) return res;
      
      Set<String> visited = new HashSet<>();
      Queue<String> queue = new LinkedList<>();
      
      // initialize
      queue.add(s);
      visited.add(s);
      
      boolean found = false;
      
      while (!queue.isEmpty()) {
        s = queue.poll();
        
        if (isValid(s)) {
          // found an answer, add to the result
          res.add(s);
          found = true;
        }
      
        if (found) continue;
      
        // generate all possible states
        for (int i = 0; i < s.length(); i++) {
          // we only try to remove left or right paren
          if (s.charAt(i) != '(' && s.charAt(i) != ')') continue;
        
          String t = s.substring(0, i) + s.substring(i + 1);
        
          if (!visited.contains(t)) {
            // for each state, if it's not visited, add it to the queue
            queue.add(t);
            visited.add(t);
          }
        }
      }
      
      return res;
    }
    
    // helper function checks if string s contains valid parantheses
    boolean isValid(String s) {
      int count = 0;
    
      for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c == '(') count++;
        if (c == ')' && count-- == 0) return false;
      }
    
      return count == 0;
    }
}
"""

class Solution(object):
  def solve2(self, s):
    ans = []
    self.remove(s, ans, 0, 0, ['(', ')'])
    return ans

  def remove(self, s, ans, last_i, last_j, par):
    stack = 0
    for i in range(last_i, len(s)):
      if s[i] == par[0]: stack += 1
      if s[i] == par[1]: stack -= 1
      if stack >= 0: continue
      for j in range(last_j, i+1):
        if s[j] == par[1] and (j==last_j or s[j-1]!=par[1]):
          self.remove(s[:j]+s[j+1:], ans, i, j, par)
      return
    s_rev = s[::-1]
    if par[0] == '(': # finished left to right
      self.remove(s_rev, ans, 0, 0, [')', '(']);
    else:
      ans.append(s_rev)

  def removeInvalidParentheses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    result = [""]
    n = len(s)
    if n == 0: return result
    stat = []

    result = set()
    result.add("")
    i = 0
    while i < n:
      print i,
      if i == 0:
        if s[0] == '(': stat.append(1)
        else: stat.append(-1)
      else:
        if s[i] == '(': stat.append(stat[-1]+1)
        elif s[i] == ')': stat.append(stat[-1]-1)
        else: stat.append(stat[-1])
      
      new_result = set()
      for item in result:
        new_result.add(item+s[i])
      result = new_result
      
      print 'result before: ', result, len(result)
      # case 1: -1
      # remove any ) in result
      if stat[-1] == -1:
        new_result = set()
        for str_ in result:
          if str_ == "": new_result.add(str_)
          else:
            for j in range(len(str_)):
              if str_[j] == ')':
                print j
                new_result.add(str_[:j]+str_[j+1:])
        result = new_result
        stat = stat[:-1]
      print 'after: ', result, stat
      # if i == 3: break
      i += 1
    return list(result)
 
if __name__ == "__main__":
  a = Solution()
  # print a.removeInvalidParentheses("()())())")
  # print a.removeInvalidParentheses("(a)())()")

  # print a.solve2("()(")
  print a.solve2("()())())((")
