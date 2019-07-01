class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0] * num_people
        base = 0
        dist = num_people * (num_people + 1) // 2
        while candies > 0:
            total = base * num_people + dist
            if total <= candies:
                candies -= total
                # full += 1
                for i in range(num_people):
                    res[i] += base + i + 1
                base += num_people
            else:
                i = 0
                while candies > 0:
                    if candies > base + i + 1:
                        res[i] += base + i + 1
                        candies -= base + i + 1
                    else:
                    	res[i] += candies
                    	candies = 0
                    i += 1
            print(res)
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.distributeCandies(100, 3))