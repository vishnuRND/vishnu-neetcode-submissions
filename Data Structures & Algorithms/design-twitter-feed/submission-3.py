class Twitter:

    def __init__(self):
        self.count = 1
        self.newsFeed = defaultdict(deque)
        self.followers = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.newsFeed:
            self.newsFeed[userId] = deque()
        if len(self.newsFeed[userId]) == 10:
            self.newsFeed[userId].popleft()
        self.count += 1
        self.newsFeed[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = [[cnt,twtid] for cnt,twtid in self.newsFeed[userId]]
        heapq.heapify(tweets)
        for follower in self.followers[userId]:
            for count, tweet in self.newsFeed[follower]:
                if len(tweets) == 10:
                    if tweets[0][0] < count:
                        heapq.heappop(tweets)
                        heapq.heappush(tweets,[count, tweet])
                else:
                    heapq.heappush(tweets,[count, tweet])
        
        result = list()
        while tweets:
            result.append(heapq.heappop(tweets)[1])
        result.reverse()
        return result

       
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
