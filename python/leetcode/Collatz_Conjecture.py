"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

"""
https://en.wikipedia.org/wiki/Collatz_conjecture
"""

def collatz():
    memo = {1: 1}
    best = 1
    for i in range(1, 10**6):
        if i in memo:
            continue
        tmp = [i]
        while tmp[-1] not in memo:
            item = tmp[-1]
            if item % 2 == 0:
                item //= 2
            else:
            	item = 3 * item + 1
            tmp.append(item)
        item = tmp[-1]
        c = memo[item]
        _ = tmp.pop()
        while len(tmp) > 0:
            c += 1
            item = tmp.pop()
            memo[item] = c
        if memo[item] > memo[best]:
            best = item
    print(best, memo[best])
    return best


if __name__ == "__main__":
    print(collatz()) 