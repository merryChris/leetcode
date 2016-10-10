class Solution(object):
  ### 400. Nth Digit ###
  # @param {integer} n
  # @return {integer}
  def findNthDigit(self, n):
    if not n: return 0

    cnt, size = 9, 1
    while cnt*size < n:
      n -= cnt*size
      cnt *= 10
      size += 1
    num = 10 ** (size-1) + (n-1) // size
    return int(str(num)[(n-1)%size])

  ### 401. Binary Watch ###
  # @param {integer} num
  # @return {string[]}
  def readBinaryWatch(self, num):
    def dfs(cur, left, num, val, end, rec, up):
      if cur == end or left == 0:
        if left == 0 and val <= up: rec.append(val)
        return
      dfs(cur+1, left-1, num, val|(1<<cur), end, rec, up)
      dfs(cur+1, left, num, val, end, rec, up)

    res = []
    for i in range(min(num+1,4)):
      hour = []
      dfs(0, i, i, 0, 4, hour, 11)
      for x in hour:
        if num-i >= 6: continue
        minute = []
        dfs(0, num-i, num-i, 0, 6, minute, 59)
        for y in minute:
          res.append("%d:%02d" % (x, y))
    return res

  ### 402. Remove K Digits ###
  # @param {string} num
  # @param {integer} k
  # @return {string}
  def removeKdigits(self, num, k):
    if not k: return num
    if k >= len(num): return '0'

    stack = []
    for c in num:
      while stack and stack[-1] > c and k:
        stack.pop()
        k -= 1
      if stack or c != '0': stack.append(c)
    while k and stack:
      stack.pop()
      k -= 1
    return ''.join(stack) or '0'

  ### 403. Frog Jump ###
  # @param {integer[]} stones
  # @return {boolean}
  def canCross(self, stones):
    if not stones: return True

    dp, rec = [[] for _ in range(len(stones))], {}
    dp[0].append(0)
    for i in range(len(stones)): rec[stones[i]] = i
    for i in range(len(stones)):
      for j in dp[i]:
        for k in (j+1,j,j-1):
          if k > 0 and stones[i]+k in rec and (not dp[rec[stones[i]+k]] or dp[rec[stones[i]+k]][-1] > k):
            dp[rec[stones[i]+k]].append(k)
            if rec[stones[i]+k] == len(stones)-1: return True

    return False

  ### 404. Sum of Left Leaves ###
  # @param {TreeNode} param
  # @return {integer}
  def sumOfLeftLeaves(self, root):
    if not root: return 0
    if not root.left and not root.right: return 0

    if root.left and not root.left.left and not root.left.right: return root.left.val + self.sumOfLeftLeaves(root.right)
    return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

  ### 405. Convert a Number to Hexadecimal ###
  # @param {integer} num
  # @return {string}
  def toHex(self, num):
    if not num: return '0'
    if num < 0: num += 2**32

    res = ''
    while num:
      cur = num & 15
      if cur == 0: res = '0'+res
      elif cur < 10: res = chr(cur+48)+res
      else: res = chr(cur%10+97)+res
      num >>= 4

    return res

  ### 406. Queue Reconstruction by Height ###
  # @param {integer[][]} people
  # @return {integer[][]}
  def reconstructQueue(self, people):
    if not people: return []

    res = []
    for p in sorted(people, key=lambda x: (-x[0], x[1])):
      res.insert(p[1], p)

    return res

  ### 407. Trapping Rain Water II ###
  # @param {integer[][]} heightMap
  # @return {integer}
  def trapRainWater(self, heightMap):
    if not heightMap: return 0

    import heapq
    m, n = len(heightMap), len(heightMap[0])
    queue, vis, res = [], [[False]*n for _ in range(m)], 0
    for i in range(m):
      queue.append((heightMap[i][0], (i,0)))
      queue.append((heightMap[i][n-1], (i,n-1)))
      vis[i][0] = vis[i][n-1] = True
    for i in range(1,n-1):
      queue.append((heightMap[0][i], (0,i)))
      queue.append((heightMap[m-1][i], (m-1,i)))
      vis[0][i] = vis[m-1][i] = True
    heapq.heapify(queue)
    while queue:
      val, loc = heapq.heappop(queue)
      res += val - heightMap[loc[0]][loc[1]]
      for d in [[-1,0],[0,1],[1,0],[0,-1]]:
        tx, ty = loc[0]+d[0], loc[1]+d[1]
        if 0 < tx < m and 0 < ty < n and not vis[tx][ty]:
          vis[tx][ty] = True
          heapq.heappush(queue, (max(val, heightMap[tx][ty]), (tx, ty)))

    return res

  ### 409. Longest Palindrome ###
  # @param {string} s
  # @return {integer}
  def longestPalindrome(self, s):
    if not s: return 0

    cnt, odd, rec = 0, 0, {}
    for c in s:
      if c not in rec: rec[c] = 0
      rec[c] += 1
    for _, v in rec.items():
      cnt += v // 2
      if v & 1: odd = 1

    return (cnt << 1) + odd
