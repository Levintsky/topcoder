"""
679. 24 Game (Hard)

You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""

"""
backtracking

class Solution {

    boolean res = false;
    final double eps = 0.001;

    public boolean judgePoint24(int[] nums) {
        List<Double> arr = new ArrayList<>();
        for(int n: nums) arr.add((double) n);
        helper(arr);
        return res;
    }

    private void helper(List<Double> arr){
        if(res) return;
        if(arr.size() == 1){
            if(Math.abs(arr.get(0) - 24.0) < eps)
                res = true;
            return;
        }
        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < i; j++) {
                List<Double> next = new ArrayList<>();
                Double p1 = arr.get(i), p2 = arr.get(j);
                next.addAll(Arrays.asList(p1+p2, p1-p2, p2-p1, p1*p2));
                if(Math.abs(p2) > eps)  next.add(p1/p2);
                if(Math.abs(p1) > eps)  next.add(p2/p1);
                
                arr.remove(i);
                arr.remove(j);
                for (Double n: next){
                    arr.add(n);
                    helper(arr);
                    arr.remove(arr.size()-1);
                }
                arr.add(j, p2);
                arr.add(i, p1);
            }
        }
    }
}
"""

class Solution(object):
	def solve2(self, nums):
        # solution 2: can AC
    	from operator import truediv, mul, add, sub
    	from fractions import Fraction

    	def apply(A, B):
        	ans = set()
        	for x, y, op in itertools.product(A, B, (truediv, mul, add, sub)):
            	if op is not truediv or y: ans.add(op(x, y))
            	if op is not truediv or x: ans.add(op(y, x))
        	return ans
    
    	A = [{x} for x in map(Fraction, nums)]
    	for i, j in itertools.combinations(range(4), 2):
        	r1 = apply(A[i], A[j])
        	k, l = {0, 1, 2, 3} - {i, j}
        	if 24 in apply(apply(r1, A[k]), A[l]): return True
        	if 24 in apply(apply(r1, A[l]), A[k]): return True
        	if 24 in apply(r1, apply(A[k], A[l])): return True
    
    	return False

    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # step 1: generate all nums
        orders = self.generate_orders(3)
        # step 2: generate *, /, +, -
        ops = self.generate2(3)
        # step 3: generate orders
        for order in orders:
            for op in ops:

                tmp = []

                numbers = []
                for o in order:
                    numbers.append(nums[o])
                for i in range(3):
                    tmp.append(str(float(numbers[i])))
                    tmp.append(op[i])
                tmp.append(str(float(numbers[3])))
                # print tmp

                val1 = '((' + tmp[0] + tmp[1] + tmp[2]+')'+tmp[3]+tmp[4]+')'+tmp[5]+tmp[6]
                try:
                    if abs(eval(val1) - 24.0) < .1:
                        return True
                except ZeroDivisionError:
                    pass
                val2 = '(' + tmp[0] + tmp[1] + tmp[2]+')'+tmp[3]+ '('+tmp[4]+tmp[5]+tmp[6]+')'
                try:
                    if abs(eval(val2) - 24.0) < .1:
                        return True
                except ZeroDivisionError:
                    pass
                val3 = '(' + tmp[0] + tmp[1] + '(' + tmp[2]+tmp[3]+ tmp[4]+'))'+tmp[5]+tmp[6]
                try:
                    if abs(eval(val3) - 24.0) < .1:
                        return True
                except ZeroDivisionError:
                    pass
                val4 = tmp[0] + tmp[1] + '((' + tmp[2]+tmp[3]+ tmp[4]+')'+tmp[5]+tmp[6]+')'
                try:
                    if abs(eval(val4) - 24.0) < .1:
                        return True
                except ZeroDivisionError:
                    pass
                val5 = tmp[0] + tmp[1] + '(' + tmp[2]+tmp[3]+ '('+tmp[4]+tmp[5]+tmp[6]+'))'
                try:
                    if abs(eval(val5) - 24.0) < .1:
                        return True
                except ZeroDivisionError:
                    pass

        # if close enough return 0
        return False

    def generate2(self, k):
        l_ = ['+', '-', '*', '/']
        result = ['']
        new_result = []
        for i in range(k):
          new_result = []
          for tmp in result:
             for c in l_:
               new_result.append(tmp+c)
          result, new_result = new_result, []
        return result

    def generate_orders(self, n):
        result = [[0]]
        new_result = []
        for i in range(1, n+1):
          new_result = []
          for sub_list in result:
              for j in range(i+1):
                  a = [item for item in sub_list]
                  a.insert(j, i)
                  new_result.append(a)
          result, new_result = new_result, []
        return result
