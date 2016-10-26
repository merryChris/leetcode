class Solution:
  ### 371. Sum of Two Integers ###
  # @param {integer} a
  # @param {integer} b
  # @return {integer}
  def getSum(self, a, b):
    c, cur, jin = 0, 0, 0
    while cur < 32 and (a or b or jin):
      c |= ((a&1) ^ (b&1) ^ jin) << cur
      jin = (a&1&jin) | (b&1&jin) | (a&b&1)
      a >>= 1
      b >>= 1
      cur += 1

    if c+1 > (1<<31): c -= (1 << 32)
    return c

  ### 372. Super Pow ###
  # @param {integer} a
  # @param {integer[]} b
  # @return {integer}
  def superPow(self, a, b):
    return pow(a, reduce(lambda x, y: (x*10+y)%1140, b)+1140, 1337)

  ### 373. Find K Pairs with Smallest Sums ###
  # @param {integer[]} nums1
  # @param {integer[]} nums2
  # @param {integer} k
  # @return {integer[][]
  def kSmallestPairs(self, nums1, nums2, k):
    if not nums1 or not nums2 or not k: return []
    if len(nums1)*len(nums2) <= k: return [[a, b] for a in nums1 for b in nums2]

    import heapq
    def push(q, i, j):
      heapq.heappush(q, [nums1[i]+nums2[j], i, j])

    if len(nums1) > k: del nums1[k:]
    if len(nums2) > k: del nums2[k:]
    queue, res = [], []
    push(queue, 0, 0)

    while len(res) < k:
      _, i, j = heapq.heappop(queue)
      res.append([nums1[i], nums2[j]])
      if j < len(nums2)-1: push(queue, i, j+1)
      if j == 0 and i < len(nums1)-1: push(queue, i+1, j)

    return res

  ### 374. Guess Number Higher or Lower ###
  # @param {integer} n
  # @return {integer}
  def guessNumber(self, n):
    l, r = 1, n
    while l <= r:
      mid = (l+r) >> 1
      val = guess(mid)
      if val == 0: return mid
      elif val == 1: l = mid+1
      else: r = mid-1
    return -1

  ### 375. Guess Number Higher or Lower II ###
  # @param {integer} n
  # @param {integer}
  def getMoneyAmount(self, n):
    from collections import deque
    dp = [[0]*(n+1) for _ in range(n+1)]
    for j in range(2,n+1):
      k = j-1
      dq = deque()
      for i in range(j-1, 0, -1):
        while k >= i and dp[i][k-1] > dp[k+1][j]:
          if len(dq) > 0 and dq[0][1] == k: dq.popleft()
          k -= 1
        val = i + dp[i+1][j]
        while len(dq) > 0 and dq[-1][0] > val: dq.pop()
        dq.append((val, i))
        dp[i][j] = min(dp[i][k]+k+1, dq[0][0])

    return dp[1][n]

  ### 376. Wiggle Subsequence ###
  # @param {integer[]} nums
  # @return {intger}
  def wiggleMaxLength(self, nums):
    if not nums: return 0
    if len(nums) == 1: return 1

    res, flag = 1, nums[0] < nums[1]
    for i in range(1, len(nums)):
      if (flag and nums[i] > nums[i-1]) or (not flag and nums[i] < nums[i-1]):
        flag ^= 1
        res += 1

    return res

  ### 377. Combination Sum IV ###
  # @param {integer[]} nums
  # @param {integer} target
  # @return {integer}
  def combinationSum4(self, nums, target):
    if not nums or not target: return 0

    nums.sort()
    dp = [1] + [0] * target
    for i in range(1, target+1):
      for j in range(len(nums)):
        if nums[j] > i: break
        dp[i] += dp[i-nums[j]]

    return dp[-1]

  ### 378. Kth Smallest Element in a Sorted Matrix ###
  # @param {integer[][]} matrix
  # @param {integer} k
  # @return {integer}
  def kthSmallest(self, matrix, k):
    import heapq
    def push(q, i, j):
      if i < len(matrix) and j < len(matrix[0]):
        heapq.heappush(q, (matrix[i][j], i, j))

    queue, res = [], matrix[0][0]
    push(queue, 0, 0)

    for _ in range(k):
      res, i, j = heapq.heappop(queue)
      if j < k-1: push(queue, i, j+1)
      if j == 0 and i < k-1: push(queue, i+1, j)

    return res

  ### 383. Ransom Note ###
  # @param {string} ransomNote
  # @param {string} magazine
  # @return {boolean}
  def canConstruct(self, ransomNote, magazine):
    rec, flag = [0] * 26, True
    for l in magazine:
      rec[ord(l)-97] += 1
    for l in ransomNote:
      if rec[ord(l)-97] == 0:
        flag = False
        break
      rec[ord(l)-97] -= 1

    return flag

  ### 385. Mini Parser ###
  # @param {string} s
  # @return {NestedInteger}
  def deserialize(self, s):
    ss = eval(s)

    def dfs(data):
      if isinstance(data, list):
        res = NestedInteger()
        for d in data:
          res.add(dfs(d))
        return res
      return NestedInteger(data)

    return dfs(ss)

  ### 386. Lexicographical Numbers ###
  # @param {integer} n
  # @return {interger[]}
  def lexicalOrder(self, n):
    if not n: return []

    def find_next(cur, n):
      if cur and cur*10 <= n: return cur*10
      if cur%10 != 9 and cur+1 <= n: return cur+1
      cur /= 10
      while cur%10 == 9: cur /= 10
      return cur+1

    res, now = [], 0
    for _ in xrange(n):
      now = find_next(now, n)
      res.append(now)

    return res

  ### 387. First Unique Character in a String ###
  # @param {string} s
  # @return {integer}
  def firstUniqChar(self, s):
    if not s: return -1

    cnt, loc, res = [0] * 26, [-1] * 26, -1
    for i in range(len(s)):
      cnt[ord(s[i])-97] += 1
      loc[ord(s[i])-97] = i
    for i in range(26):
      if cnt[i] == 1:
        if res == -1 or loc[i] < res:
          res = loc[i];
    return res
