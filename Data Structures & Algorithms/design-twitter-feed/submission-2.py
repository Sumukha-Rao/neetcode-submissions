from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=defaultdict(list)
        self.following=defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        users=self.following[userId] | {userId}
        for user in users:
            if self.tweets[user]:
                idx=len(self.tweets[user])-1
                time,tweetId=self.tweets[user][idx]
                heapq.heappush(heap,(-time,tweetId,user,idx))
        feed=[]
        while heap and len(feed)<10:
            negTime,tweetId,user,idx=heapq.heappop(heap)
            feed.append(tweetId)
            if idx>0:
                idx-=1
                time,tweetId=self.tweets[user][idx]
                heapq.heappush(heap,(-time,tweetId,user,idx))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId !=followeeId:
            self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
