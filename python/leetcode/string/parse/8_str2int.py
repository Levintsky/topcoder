'''
8. String to Integer (atoi) (Medium)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
'''

"""
problem definition:
 1. integer! (not float)
 2. integer always valid?
edge condition:
 1. starting spaces;
 2. +/-;
 3. > INT_MAX; < INT_MIN; trim and return;
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == "": return 0
        i = 0
        n = len(str)

        # step 0: discarding spaces
        while i < n and str[i] == " ": i += 1
        
        if i != n:
            if str[i] == '-':
                neg = True
                i += 1
            elif str[i] == '+':
                i += 1
                neg = False
            else:
                neg = False
       
        print i, str[i:] 
        result = 0
        j = i
        while j < n and ord(str[j]) >= ord('0') and ord(str[j]) <= ord('9'):
            result = result * 10 + ord(str[j]) - ord('0')
            j += 1
        if neg:
            result = -result
        return result


if __name__ == "__main__":
  a = Solution()
  print a.myAtoi("+-2")
