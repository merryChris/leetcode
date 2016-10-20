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
