from sortedcontainers import SortedList
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ownfeed={
        }
        self.connect={
        }
        self.current=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.current+=1
        if userId not in self.ownfeed:
            self.ownfeed[userId]=[]
        self.ownfeed[userId].append([tweetId, self.current])
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        contain=SortedList(key = lambda x: -x[1])
        if userId in self.ownfeed:
            for i in range(len(self.ownfeed[userId])-1, max(-1, len(self.ownfeed[userId])-11),-1):
                contain.add(self.ownfeed[userId][i])
        
        if userId in self.connect:
            for follower in self.connect[userId]:
                if follower in self.ownfeed:
                    for i in range(len(self.ownfeed[follower])-1, max(-1, len(self.ownfeed[follower])-11),-1):
                        contain.add(self.ownfeed[follower][i])
       
        result=[]
        for i in range(0, min(10, len(contain))):
            if contain[i][0] not in result:
                result.append(contain[i][0])
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId!=followeeId:
            if followerId not in self.connect:
                self.connect[followerId]=[]
            self.connect[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId!=followeeId:
            if followerId in self.connect:
                try:
                    self.connect[followerId].remove(followeeId)
                except:
                    pass
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
