### 303. Range Sum Query - Immutable ###
class NumArrayI(object):

    # Initialize your data structure here.
    # @param{integer[]} nums
    def __init__(self, nums):
        if not nums: return

        self.n = len(nums)
        self.sum_array = [0]*self.n
        for i in xrange(self.n):
            self.sum_array[i] = nums[i]
            if i > 0: self.sum_array[i] += self.sum_array[i-1]

    # Sum of elements nums[i..j], inclusive.
    # @param {integer} i
    # @param {integer} j
    # @return {integer}
    def sumRange(self, i, j):
        if not (0<=i<self.n and 0<=j<self.n): return 0

        res = self.sum_array[j]
        if i > 0: res -= self.sum_array[i-1]

        return res

### 304. Range Sum Query 2D - Immutable ###
class NumMatrix(object):

    # Initialize your data structure here.
    # @param{integer[][]} matrix
    def __init__(self, matrix):
        if not matrix: return

        self.m, self.n = len(matrix), len(matrix[0])
        self.sum_matrix = [[0]*self.n for _ in range(self.m)]

        for i in xrange(self.m):
            for j in xrange(self.n):
                self.sum_matrix[i][j] = matrix[i][j]
                if i > 0: self.sum_matrix[i][j] += self.sum_matrix[i-1][j]
                if j > 0: self.sum_matrix[i][j] += self.sum_matrix[i][j-1]
                if i > 0 and j > 0: self.sum_matrix[i][j] -= self.sum_matrix[i-1][j-1]

    # Sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
    # @param {integer} row1
    # @param {integer} col1
    # @param {integer} row2
    # @param {integer} col2
    # @return {integer}
    def sumRegion(self, row1, col1, row2, col2):
        if not (0<=row1<self.m and 0<=row2<self.m and 0<=col1<self.n and 0<=col2<self.n): return 0

        res = self.sum_matrix[row2][col2]
        if row1 > 0: res -= self.sum_matrix[row1-1][col2]
        if col1 > 0: res -= self.sum_matrix[row2][col1-1]
        if row1 > 0 and col1 > 0: res += self.sum_matrix[row1-1][col1-1]

        return res

### 307. Range Sum Query - Mutable ###
class NumArray(object):

    # Initialize your data structure here.
    # @param {integer[]} nums
    def __init__(self, nums):
        if not nums: return

        self.n = len(nums)
        self.nums, self.c = [0]*self.n, [0]*(self.n+1)
        for i in xrange(self.n):
            self.update(i, nums[i])

    # @param {integer} i
    # @param {integer} val
    # @return {void}
    def update(self, i, val):
      if i >= self.n: return

      pos, delta = i+1, val-self.nums[i]
      while pos <= self.n:
          self.c[pos] += delta
          pos += pos&(-pos)
      self.nums[i] = val

    # Sum of elements nums[0..j], inclusive.
    # @param {integer} i
    # @return {integer}
    def sum(self, i):
        if not 0<=i<self.n: return 0

        pos, res = i+1, 0
        while pos > 0:
            res += self.c[pos]
            pos -= pos&(-pos)
        return res

    # Sum of elements nums[i..j], inclusive.
    # @param {integer} i
    # @param {integer} j
    # @return {integer}
    def sumRange(self, i, j):
        if not (0<=i<self.n and 0<=j<self.n and i<=j): return 0

        return self.sum(j)-self.sum(i-1)

### 341. Flatten Nested List Iterator ###
class NestedIterator(object):

    # Initialize your data structure here.
    # @param {NestedInteger[]} nestedList
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    # @return {integer}
    def next(self):
        return self.stack.pop().getInteger()

    # @return {boolean}
    def hasNext(self):
        while self.stack and not self.stack[-1].isInteger():
            top = self.stack.pop()
            self.stack += top.getList()[::-1]
        return len(self.stack)>0

### 352. Data Stream as Disjoint Intervals ###
class SummaryRanges(object):

    # Initialize your data structure here.
    def __init__(self):
        self.have, self.left, self.right = set(), {}, {}

    # @param {integer} val
    # @return {void}
    def addNum(self, val):
        if val in self.have: return

        self.have.add(val)
        if val-1 in self.right and val+1 in self.left:
            l, r = self.right.pop(val-1), self.left.pop(val+1)
            self.left.pop(l.start)
            self.right.pop(r.end)
            interval = Interval(l.start, r.end)
            self.left[l.start], self.right[r.end] = interval, interval
        elif val-1 in self.right:
            l = self.right.pop(val-1)
            self.left.pop(l.start)
            interval = Interval(l.start, val)
            self.left[l.start], self.right[val] = interval, interval
        elif val+1 in self.left:
            r = self.left.pop(val+1)
            self.right.pop(r.end)
            interval = Interval(val, r.end)
            self.left[val], self.right[r.end] = interval, interval
        else:
            interval = Interval(val, val)
            self.left[val], self.right[val] = interval, interval

    # @return {Interval[]}
    def getIntervals(self):
        return [self.left[key] for key in sorted(self.left.keys())]

### 355. Design Twitter ###
class Twitter(object):

    # Initialize your data structure here.
    def __init__(self):
        self.timestamp = 0
        self.tweets = {}
        self.follows = {}

    # Compose a new tweet.
    # @param {integer} userId
    # @param {integer} tweetId
    # @return {void}
    def postTweet(self, userId, tweetId):
        if userId not in self.tweets: self.tweets[userId] = []

        if len(self.tweets[userId]) == 10: self.tweets[userId].pop(0)
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    # Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users
    # who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
    # @param {integer} userId
    # @return {integer[]}
    def getNewsFeed(self, userId):
        cache = []
        if userId in self.tweets: cache.extend(self.tweets[userId])
        import heapq
        heapq.heapify(cache)

        if userId in self.follows:
            for fo in self.follows[userId]:
                if fo not in self.tweets: continue
                for td in self.tweets[fo]:
                    if len(cache) == 10: heapq.heappushpop(cache, td)
                    else: heapq.heappush(cache, td)

        res = []
        while cache: res.append(heapq.heappop(cache)[1])
        return res[::-1]

    # Follower follows a followee. If the operation is invalid, it should be a no-op.
    # @param {integer} followerId
    # @param {integer} followeeId
    # @return {void}
    def follow(self, followerId, followeeId):
        if followerId == followeeId: return
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    # Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    # @param {integer} followerId
    # @param {integer} followeeId
    # @return {void}
    def unfollow(self, followerId, followeeId):
        if followerId not in self.follows: return
        if followeeId not in self.follows[followerId]: return
        self.follows[followerId].remove(followeeId)

### 382. Linked List Random Node ###
class RandomNodes(object):

  # @param {ListNode} head The linked list's head.
  # Note that the head is guaranteed to be not null, so it contains at least one node.
  def __init__(self, head):
    self.head = head

  # @return {integer} Returns a random node's value.
  def getRandom(self):
    res, l, cur = 0, 0, self.head

    import random
    while cur:
      l += 1
      if int(random.random() * l) == 0:
        res = cur.val
      cur = cur.next
    return res

### 384. Shuffle an Array ###
class Solution(object):

  # @param {integer[]} nums
  def __init__(self, nums):
    self.nums = nums

  # @return {integer[]}
  # Resets the array to its original configuration and return it.
  def reset(self):
    return self.nums

  # @return {integer[]}
  # Returns a random shuffling of the array.
  def shuffle(self):
    res = [_ for _ in self.nums]
    import random
    random.shuffle(res)
    return res

### 398. Random Pick Index ###
class Solution(object):

  # @param {integer[]}
  def __init__(self, nums):
    self.nums = nums

  # @param {integer} target
  # @return {integer}
  def pick(self, target):
    import random
    idx, cnt = -1, 0
    for i, num in enumerate(self.nums):
      if num == target:
        if random.randint(0, cnt) == 0: idx = i
        cnt += 1

    return idx
