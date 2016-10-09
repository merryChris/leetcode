class Solution(object):
  ### 410. Split Array Largest Sum ###
  # @param {integer[]} nums
  # @param {integer} m
  # @return {integer}
  def splitArray(self, nums, m):
    if not nums: return 0
    if m == 1: return sum(nums)

    def check(bound):
      cur, pos, cnt = 0, 0, 1
      while pos < len(nums) and cnt <= m:
        if cur+nums[pos] <= bound:
          cur += nums[pos]
        else:
          cur = nums[pos]
          cnt += 1
        pos += 1
      return pos == len(nums) and cnt <= m

    l, r = max(nums), sum(nums)
    while l <= r:
      mid = (l+r) >> 1
      if check(mid): r = mid-1
      else: l = mid+1
    return l

  ### 415. Add Strings ###
  # @param {string} num1
  # @param {string} num2
  # @return {string}
  def addStrings(self, num1, num2):
    if not num1: return num2
    if not num2: return num1

    pos, carry, res = 0, 0, ""
    l1, l2 = len(num1), len(num2)
    while pos < l1 or pos < l2 or carry:
      a = pos < l1 and ord(num1[l1-1-pos])-48 or 0
      b = pos < l2 and ord(num2[l2-1-pos])-48 or 0
      res += chr(48+(a+b+carry)%10)
      carry = (a+b+carry) // 10
      pos += 1

    return res[::-1]

  ### 416. Partition Equal Subset Sum ###
  # @param {integer[]} nums
  # @return {boolean}
  def canPartition(self, nums):
    if not nums: return True
    if sum(nums) & 1: return False

    n = sum(nums) >> 1
    dp = [False] * (n+1)
    dp[0] = True
    for num in nums:
      for i in range(n,num-1,-1):
        dp[i] |= dp[i-num]
      if dp[n]: break
    return dp[n]


  ### 417. Pacific Atlantic Water Flow ###
  # @param {integer[][]} matrix
  # @return {integer[][]}
  def pacificAtlantic(self, matrix):
    if not matrix or not matrix[0]: return []

    MOVE = ((-1,0), (0,1), (1,0), (0,-1))
    m, n = len(matrix), len(matrix[0])
    queue, res, rec = [], [], [[0]*n for _ in range(m)]
    def bfs():
      vis = [[False]*n for _ in range(m)]
      while queue:
        cur = queue.pop(0)
        if vis[cur[0]][cur[1]]: continue
        vis[cur[0]][cur[1]] = True
        if rec[cur[0]][cur[1]] == 1: res.append([cur[0], cur[1]])
        rec[cur[0]][cur[1]] ^= 1
        for i in range(4):
          tx, ty = cur[0]+MOVE[i][0], cur[1]+MOVE[i][1]
          if tx >= 0 and tx < m and ty >= 0 and ty < n and not vis[tx][ty] and \
             matrix[tx][ty] >= matrix[cur[0]][cur[1]]: queue.append((tx, ty))
    for i in range(n): queue.append((0,i))
    for i in range(1,m): queue.append((i,0))
    bfs()
    for i in range(n): queue.append((m-1,i))
    for i in range(m-1): queue.append((i,n-1))
    bfs()

    return res
