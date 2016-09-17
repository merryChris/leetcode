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
