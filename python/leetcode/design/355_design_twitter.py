'''
355. Design Twitter (Medium)

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.

Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
'''

class Twitter(object):
  def __init__(self):
    self.twit_list = [] # a list of (userid, tweetid) tuples, newest at the last
    self.follow_map = {}

  def postTweet(self, userId, tweetId):
    self.twit_list.append((userId, tweetId))

  def getNewsFeed(self, userId):
    result = []
    i = len(self.twit_list)-1
    while(i>=0 and len(result)<10):
      tmp_u, tmp_t = self.twit_list[i]
      if tmp_u == userId or (userId in self.follow_map and tmp_u in self.follow_map[userId]):
        result.append(tmp_t)
      i -= 1
    return result

  def follow(self, followerId, followeeId):
    if followerId not in self.follow_map:
      self.follow_map[followerId] = set()
    self.follow_map[followerId].add(followeeId)

  def unfollow(self, followerId, followeeId):
    if followerId in self.follow_map and followeedId in self.follow_map[followerId]:
      self.follow_map[followerId].remove(followeeId)


if __name__ == '__main__':
  x = Twitter()
  x.postTweet(2,5)
  x.follow(1, 2)
  x.follow(1, 2)
  print x.getNewsFeed(1)
  # x.unfollow(1, 2)
  # print x.getNewsFeed(1)
