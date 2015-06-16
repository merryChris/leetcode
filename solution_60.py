class Solution:
    ### 60. Permutation Sequence ###
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        nums, fac, res = [x+1 for x in xrange(n)], [1], ''
        for i in xrange(1,n): fac.append(fac[i-1]*i)
        for i in xrange(n,0,-1):
            idx = (k-1) / fac[i-1]
            res += str(nums.pop(idx))
            k %= fac[i-1]

        return res

    ### 61. Rotate List ###
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head or k == 0: return head

        cur, l = head, 0
        while cur:
            l += 1
            if not cur.next: break
            cur = cur.next
        k %= l
        if k == 0: return head

        cur.next = head
        for _ in xrange(l-k):
            cur = cur.next
        head = cur.next
        cur.next = None

        return head

    ### 62. Unique Paths ###
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        a = m+n-2
        b = min(m,n)-1
        if b == 0: return 1
        c = [[0]*(b+1) for _ in xrange(a+1)]
        for _ in xrange(b+1): c[_][_] = 1
        for _ in xrange(a+1): c[_][0] = 1
        for i in xrange(1,a+1):
            for j in xrange(1,b+1):
                if i == j: continue
                c[i][j] = c[i-1][j-1] + c[i-1][j]

        return c[a][b]

    ### 63. Unique Paths II ###
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1: return 0

        dp = [[0]*n for _ in xrange(m)]
        dp[0][0] = 1
        for i in xrange(m):
             for j in xrange(n):
                 if obstacleGrid[i][j] == 1: continue
                 if i>0: dp[i][j] += dp[i-1][j]
                 if j>0: dp[i][j] += dp[i][j-1]

        return dp[m-1][n-1]

    ### 64. Minimum Path Sum ###
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        if not grid: return 0

        m, n = len(grid), len(grid[0])
        dp = [[float('inf')]*n for _ in xrange(m)]
        dp[0][0] = grid[0][0]
        for l in xrange(1,m+n-1):
            for i in xrange(max(0,l-n+1),min(m,l+1)):
                j = l-i
                if i>0: dp[i][j] = min(dp[i][j], dp[i-1][j]+grid[i][j])
                if j>0: dp[i][j] = min(dp[i][j], dp[i][j-1]+grid[i][j])

        return dp[m-1][n-1]

    ### 65. Valid Number ###
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        try:
            float(s)
        except:
            return False
        return True

    ### 66. Plus One ###
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        return map(int, list(str(int(''.join(map(str, digits)))+1)))

    ### 67. Add Binary ###
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        return '{:b}'.format(int(a,2)+int(b,2))

    ### 68. Text Justification ###
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, word, maxWidth):
        text, cur, tot = [], [], 0

        def make(isLastOne=False):
            if isLastOne:
                res = ' '.join(cur)
                return res + ' '*(maxWidth-len(res))

            cnt = len(cur)
            left = maxWidth-tot+cnt-1
            res = ''
            for i in xrange(cnt):
                if i > 0:
                    c = left/(cnt-1)
                    if left%(cnt-1):
                        c += 1
                        left -= 1
                    res += ' '*c
                res += cur[i]
            if cnt == 1: res += ' '*left

            return res

        while word:
            l = len(word[0])
            if tot: l += 1
            if tot+l <= maxWidth:
                tot += l
                cur.append(word.pop(0))
            else:
                text.append(make())
                cur, tot = [], 0
        text.append(make(isLastOne=True))

        return text

    ### 69. Sqrt(x) ###
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = (l+r)>>1
            if mid*mid > x: r = mid-1
            else: l = mid+1

        return r
