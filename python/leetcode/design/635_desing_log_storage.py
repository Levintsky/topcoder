"""
635. Design Log Storage System My SubmissionsBack to Contest (Medium)

You are given several logs that each log contains a unique id and timestamp. Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.


int[] Retrieve(String start, String end, String granularity): Return the id of logs whose timestamps are within the range from start to end. Start and end all have the same format as timestamp. However, granularity means the time level for consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

Example 1:
put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], because you need to return all logs within 2016 and 2017.
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.
Note:
There will be at most 300 operations of Put or Retrieve.
Year ranges from [2000,2017]. Hour ranges from [00,23].
Output for Retrieve has no order required.
"""


class LogSystem(object):
    def __init__(self):
        self.data = []
        return

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        timestamp_l = timestamp.split(":")
        timestamp_l = [int(item) for item in timestamp_l]
        self.data.append((id, timestamp_l))

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        s_l = s.split(":")
        s_l = [int(item) for item in s_l]
        e_l = e.split(":")
        e_l = [int(item) for item in e_l]
        gra_l = -1
        if gra == "Year":
            gra_l = 0
        elif gra == "Month":
            gra_l = 1
        elif gra == "Day":
            gra_l = 2
        elif gra == "Hour":
            gra_l = 3
        elif gra == "Minute":
            gra_l = 4
        else:
            gra_l = 5
        result = []
        for item in self.data:
            id, tmp = item
            if self.helper_smaller(s_l, tmp, gra_l) and self.helper_smaller(
                tmp, e_l, gra_l
            ):
                result.append(id)
        return result

    def helper_smaller(self, s_l, tmp, gra):
        """s_l1 = tuple(s_l[:gra+1])
        tmp1 = tuple(tmp[:gra+1])
        return s_l1 <= tmp1"""
        return tuple(s_l[: gra + 1]) <= tuple(tmp[: gra + 1])

    def helper_larger(self, tmp, e_l, gra):
        return tuple(tmp[: gra + 1]) <= tuple(e_l[: gra + 1])


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
