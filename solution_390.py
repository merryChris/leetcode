class Solution:
  ### 390. Elimination Game ###
  # @param {integer} n
  # @return {integer}
  def lastRemaining(self, n):
    if n <= 1: return 1

    def dfs(n, d):
      if (n == 1): return 1
      if d == 0 or n & 1: return dfs(n >> 1, d^1) << 1
      return (dfs(n >> 1, d^1) << 1) - 1

    return dfs(n, 0)

  ### 391. Perfect Rectangle ###
  # @param {integer[][]} rectangles
  # @return {boolean}
  def isRectangleCover(self, rectangles):
    if not rectangles: return False

    corner, area, hsh, cnt = rectangles[0][:], 0, {}, [0]*5
    for r in rectangles:
      area += (r[0]-r[2]) * (r[1]-r[3])
      corner[0] = min(corner[0], r[0])
      corner[1] = min(corner[1], r[1])
      corner[2] = max(corner[2], r[2])
      corner[3] = max(corner[3], r[3])
      if (r[0], r[1]) not in hsh: hsh[(r[0], r[1])] = 1
      else: hsh[r[0], r[1]] += 1
      if (r[0], r[3]) not in hsh: hsh[(r[0], r[3])] = 1
      else: hsh[r[0], r[3]] += 1
      if (r[2], r[1]) not in hsh: hsh[(r[2], r[1])] = 1
      else: hsh[r[2], r[1]] += 1
      if (r[2], r[3]) not in hsh: hsh[(r[2], r[3])] = 1
      else: hsh[r[2], r[3]] += 1
    for v in hsh.values():
      if v > 4: return False
      cnt[v] += 1

    if hsh.get((corner[0],corner[1])) != 1 or hsh.get((corner[0],corner[3])) != 1 or \
       hsh.get((corner[2],corner[1])) != 1 or hsh.get((corner[2],corner[3])) != 1: return False
    if cnt[1] != 4 or cnt[2] & 1 or cnt[3]: return False
    return area == (corner[0]-corner[2]) * (corner[1]-corner[3])

  ### 392. Is Subsequence ###
  # @param {string} s
  # @param {string} t
  # @return {boolean}
  def isSubsequence(self, s, t):
    if not s: return True
    if not t: return False

    ps, pt = 0, 0
    while ps < len(s) and pt < len(t):
      if s[ps] == t[pt]: ps += 1
      pt += 1

    return ps == len(s)

  ### 393. UTF-8 Validation ###
  # @param {integer[]} data
  # @return {boolean}
  def validUtf8(self, data):
    if not data: return True

    h1, h2, h3, h4, h5 = 1 << 7, 1 << 6, 1 << 5, 1 << 4, 1 << 3

    def check(pos):
      if data[pos] >> 7 == 0: return 1
      if data[pos] >> 5 == 0b110:   return pos < len(data)-1 and 2 or 0
      if data[pos] >> 4 == 0b1110:  return pos < len(data)-2 and 3 or 0
      if data[pos] >> 3 == 0b11110: return pos < len(data)-3 and 4 or 0
      return 0

    loc = 0
    while loc < len(data):
      delta = check(loc)
      if delta == 0: return False
      while delta > 1:
        loc += 1
        if data[loc] >> 6 != 0b10: return False
        delta -= 1
      loc += 1
    return True

  ### 394. Decode String ###
  # @param {string} s
  # @return {string}
  def decodeString(self, s):
    if not s: return ''

    def dfs(pos):
      res = ''
      while pos < len(s) and s[pos] != ']':
        if s[pos].isalpha():
          res += s[pos]
          pos += 1
        else:
          cnt = 0
          while pos < len(s) and s[pos].isdigit():
            cnt *= 10
            cnt += int(s[pos])
            pos += 1
          tmp, pos = dfs(pos+1)
          res += tmp*cnt
          pos += 1
      return res, pos

    return dfs(0)[0]

  ### 395. Longest Substring with At Least K Repeating Characters ###
  # @param {string} s
  # @param {integer} k
  # @return {integer}
  def longestSubstring(self, s, k):
    if not s: return 0
    if not k: return len(s)

    for c in set(s):
      if s.count(c) < k:
        return max(self.longestSubstring(t, k) for t in s.split(c))

    return len(s)

  ### 396. Rotate Function ###
  # @param {integer[]} A
  # @return {integer}
  def maxRotateFunction(self, A):
    if not A: return 0

    cur, tot = reduce(lambda x, i: x+i*A[i], range(len(A)), 0), sum(A)
    res = cur
    for i in range(len(A)-1):
      cur = cur + tot - len(A)*A[len(A)-1-i]
      res = max(res, cur)

    return res

  ### 397. Integer Replacement ###
  # @param {integer} n
  # @return {integer}
  def integerReplacement(self, n):
    if n == 1: return 0

    cnt = 0
    while n != 1:
      if n & 1: n = n>3 and (n-1)/2 & 1 and n+1 or n-1
      else: n >>= 1
      cnt += 1
    return cnt

  ### 399. Evaluate Division ###
  # @param {string[][]} equations
  # @param {float[]} values
  # @param {string[][]} queries
  # @param {float[]}
  def calcEquation(self, equations, values, queries):
    if not queries: return []

    n, hsh, res = 0, {}, []
    for i in range(len(equations)):
      e  = equations[i]
      if e[0] not in hsh:
        hsh[e[0]] = n
        n += 1
      if e[1] not in hsh:
        hsh[e[1]] = n
        n += 1
    g = [['oo']*i+[1.0]+['oo']*(n-i-1) for i in range(n)]
    for i in range(len(equations)):
      e  = equations[i]
      g[hsh[e[0]]][hsh[e[1]]] = values[i]
      if values[i] != 0: g[hsh[e[1]]][hsh[e[0]]] = 1.0/values[i]
    for k in range(n):
      for i in range(n):
        if g[i][k] == 'oo':  continue
        for j in range(n):
          if g[k][j] == 'oo': continue
          g[i][j] = g[i][k] * g[k][j]
    for q in queries:
      if q[0] not in hsh or q[1] not in hsh or g[hsh[q[0]]][hsh[q[1]]] == 'oo': res.append(-1.0)
      else: res.append(g[hsh[q[0]]][hsh[q[1]]])

    return res
