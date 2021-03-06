'''
338. Counting Bits (Medium)

Given a non negative integer number num. For every numbers i in the range 0 <= i <= num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''

class Solution(object):
  def countBits(self, num):
    '''
    input: int
    output: List[int]
    '''
    if num == 0: return [0]
    result = [0, 1]
    while(len(result) < (num+1)):
      # notice the usage of x2 to reduce time
      new_result = [item+1 for item in result]
      result += new_result


    # tail = [item+1 for item in result[0:(num+1)-len(result)]
    # result = result+tail
    return result[:num+1]


if __name__ == '__main__':
  a = Solution()
  print a.countBits(5)
