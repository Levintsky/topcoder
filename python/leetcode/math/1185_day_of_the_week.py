"""
1185. Day of the Week (Easy)

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        # 1971/1/0: Thu, 1/1: Fri
        days = 0
        for y in range(1971, year):
        	if y % 4 != 0 or y == 2100:
        		days += 365
        	else:
        		days += 366
        # month
        memo_31 = {1,3,5,7,8,10,12}
        memo_30 = {4,6,9,11}
        for m in range(1, month):
        	if m in memo_31:
        		days += 31
        	elif m in memo_30:
        		days += 30
        	else: # 2
        	    if year % 4 == 0:
        	    	days += 29
        	    else:
        	    	days += 28
        # day
        days += day
        res = (days + 4) % 7
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return week[res]

    def solve2(self, day, month, year):
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        from datetime import datetime
        return days[datetime(y, m, d).weekday()]

    # The formula for this problem is Zelle formula
    # Another name: Zeller's congruence or Kim larsen calculation formula.
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ]
    def solve3(self, d, m, y):
        if m < 3:
            m += 12
            y -= 1
        c, y = y / 100, y % 100
        w = (c / 4 - 2 * c + y + y / 4 + 13 * (m + 1) / 5 + d - 1) % 7
        return self.days[w]

if __name__ == "__main__":
    a = Solution()
    print(a.dayOfTheWeek(31, 8, 2019))
    print(a.dayOfTheWeek(18, 7, 1999))
    print(a.dayOfTheWeek(15, 8, 1993))
