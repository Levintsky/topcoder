"""
1169. Invalid Transactions (Easy)

A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""

class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        memo = {} # name: (t, v, city)
        trans = []
        for tran in transactions:
            tlist = tran.split(',')
            key, t, v, city = tlist[0], int(tlist[1]), int(tlist[2]), tlist[3]
            trans.append((t, key, v, city))
        trans.sort()
        
        for tran in trans:
            t, k, v, city = tran
            if k not in memo:
                memo[k] = []
            memo[k].append((t, v, city))
        
        result = set()
        for k in memo.keys():
            last_id = 0
            for i, items in enumerate(memo[k]): # (t, v, city)
                t, v, city = items
                if v > 1000:
                    result.add(",".join([k,str(t),str(v),city]))
                flag = False
                for last_id in range(i):
                    t1, v1, city1 = memo[k][last_id]
                    if t - t1 <= 60 and city1 != city:
                        result.add(",".join([k,str(t1),str(v1),city1]))
                        flag = True

                if flag:
                    result.add(",".join([k,str(t),str(v),city]))
        result = list(result)
        result.sort()
        print(len(result))
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))
    print(a.invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"]))
    print(a.invalidTransactions(["alice,20,800,mtv","bob,50,1200,mtv"]))
