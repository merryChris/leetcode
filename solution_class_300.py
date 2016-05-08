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
