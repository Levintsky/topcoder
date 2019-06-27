"""
751. IP to CIDR (Easy)

Given a start IP address ip and a number of ips we need to cover n, 
return a representation of the range as a list (of smallest possible 
length) of CIDR blocks.

A CIDR block is a string consisting of an IP, followed by a slash, and 
then the prefix length. For example: "123.45.67.89/20". That prefix length 
"20" represents the number of common prefix bits in the specified range.

Example 1:
Input: ip = "255.0.0.7", n = 10
Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
Explanation:
The initial ip address, when converted to binary, looks like this (spaces added for clarity):
255.0.0.7 -> 11111111 00000000 00000000 00000111
The address "255.0.0.7/32" specifies all addresses with a common prefix of 32 bits to the given address,
ie. just this one address.

The address "255.0.0.8/29" specifies all addresses with a common prefix of 29 bits to the given address:
255.0.0.8 -> 11111111 00000000 00000000 00001000
Addresses with common prefix of 29 bits are:
11111111 00000000 00000000 00001000
11111111 00000000 00000000 00001001
11111111 00000000 00000000 00001010
11111111 00000000 00000000 00001011
11111111 00000000 00000000 00001100
11111111 00000000 00000000 00001101
11111111 00000000 00000000 00001110
11111111 00000000 00000000 00001111

The address "255.0.0.16/32" specifies all addresses with a common prefix of 32 bits to the given address,
ie. just 11111111 00000000 00000000 00010000.

In total, the answer specifies the range of 10 ips starting with the address 255.0.0.7 .

There were other representations, such as:
["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
but our answer was the shortest possible.

Also note that a representation beginning with say, "255.0.0.7/30" would be incorrect,
because it includes addresses like 255.0.0.4 = 11111111 00000000 00000000 00000100 
that are outside the specified range.

Note:
1. ip will be a valid IPv4 address.
2. Every implied address ip + x (for x < n) will be a valid IPv4 address.
3. n will be an integer in the range [1, 1000].
"""


class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        number = self.ip2number(ip)
        result = []
        while n > 0:
            lb = self.lowbit(number)
            while lb > n:
                lb = lb // 2

            n = n - lb

            result.append(self.number2ip(number) + "/" + str(32 - self.ilowbit(lb)))
            number = number + lb
            print(self.number2ip(number))
        return result

    def ip2number(self, ip):
        numbers = list(map(int, ip.split(".")))
        n = (numbers[0] << 24) + (numbers[1] << 16) + (numbers[2] << 8) + numbers[3]
        return n

    def number2ip(self, n):
        return ".".join(
            [str(n >> 24 & 255), str(n >> 16 & 255), str(n >> 8 & 255), str(n & 255)]
        )

    def ilowbit(self, x):
        # check the lowest bit of 1
        # 1, 3, 5, 7: 0
        # 2, 6, 10, 14: 1
        # 4, 12, 20, 28: 2
        # ...
        for i in range(32):
            if x & (1 << i):
                return i

    def lowbit(self, x):
        # count how many tail zeros
        # 1, 3, 5, 7: 1
        # 2, 6, 10: 2
        # 4, 12, 20: 4
        return 1 << self.ilowbit(x)

    def solve2(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """

        def ip2number(ip):
            nlist = ip.split(".")
            nlist = [int(item) for item in nlist]
            num = 0
            for item in nlist:
                num = num * 256 + item
            return num

        def num2ip(num):
            nlist = []
            for i in range(4):
                nlist.append(num % 256)
                num //= 256
            nlist = nlist[::-1]
            res = ".".join([str(item) for item in nlist])
            return res

        def lowbit(num):
            for i in range(32):
                if (1 << i) & num > 0:
                    return i
            raise 31

        num = ip2number(ip)
        result = []
        while n > 0:
            # step 1: find lowest bit
            bit = lowbit(num)
            curr = 2 ** bit
            while curr > n:
                curr //= 2
                bit -= 1
            n -= curr
            res = num2ip(num) + "/%d" % (32 - bit)
            result.append(res)
            num += curr
        return result


if __name__ == "__main__":
    a = Solution()
    # print(a.ipToCIDR("255.0.0.21", 200))
    print(a.solve2("255.0.0.21", 200))

    # for i in range(1, 100):
    #     print(i, a.lowbit(i))
