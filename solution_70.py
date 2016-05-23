class Solution:
    ### 70. Climbing Stairs ###
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n <= 1: return 1

        dp = [1]
        for i in xrange(1,n):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n-1]

    ### 71. Simplify Path ###
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        cur = []
        for x in path.split('/'):
            if not x or x == '.': continue
            if x != '..': cur.append(x)
            elif cur: cur.pop()

        return '/'+'/'.join(cur)

    ### 72. Edit Distance ###
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        l1, l2 = len(word1), len(word2)
        if not word1 or not word2: return max(l1, l2)

        dp = []
        for _ in xrange(l1+1): dp.append([0]*(l2+1))
        for _ in xrange(l1+1): dp[_][0] = _
        for _ in xrange(l2+1): dp[0][_] = _
        for i in xrange(l1):
            for j in xrange(l2):
                dp[i+1][j+1] = min(min(dp[i][j+1], dp[i+1][j])+1, dp[i][j]+(word1[i] != word2[j]))

        return dp[l1][l2]

    ### 73. Set Matrix Zeroes ###
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        row = []
        col = []
        for i in xrange(m):
            for j in xrange(n):
                if not matrix[i][j]:
                    if not row or row[-1] != i: row.append(i)
                    if not col or col[-1] != j: col.append(j)
        for i in row:
            for j in xrange(n):
                matrix[i][j] = 0
        for j in col:
            for i in xrange(m):
                matrix[i][j] = 0

        return

    ### 74. Search a 2D Matrix  ###
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix: return False

        def bis(nums, val):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l+r)>>1
                if nums[mid] <= val: l = mid+1
                else: r = mid-1
            return r

        m = bis([matrix[_][0] for _ in xrange(len(matrix))], target)
        if m == -1: return False
        if matrix[m][0] == target: return True
        n = bis(matrix[m], target)
        return m >= 0 and n >= 0 and matrix[m][n] == target

    ### 75. Sort Colors ###
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead
    def sortColors(self, nums):
        if not nums: return

        i, j, k = 0, 0, len(nums)-1
        while j<= k:
            if nums[j] == 0:
                if i != j: nums[i], nums[j] = nums[j], nums[i]
                i += 1; j += 1
            elif nums[j] == 1: j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1

    ### 76. Minimum Window Substring ###
    # @param {string} s
    # @oaram {string} t
    # @return {string}
    def minWindow(self, s, t):
        l = len(s)
        minWin, res = l+1, ''

        cnt, vis = [0] * 130, [False] * 130
        tot = len(set(t))
        for x in t:
            cnt[ord(x)] += 1
            vis[ord(x)] = True

        head = tail = 0
        while True:
            if tot == 0:
                while head < tail:
                    idx = ord(s[head])
                    if vis[idx] and cnt[idx] == 0: break
                    if vis[idx]: cnt[idx] += 1
                    head += 1
                if tail-head < minWin:
                    minWin = tail-head
                    res = s[head:tail]
                cnt[idx] += 1
                tot += 1
                head += 1

            if tail == l: break
            idx = ord(s[tail])
            if vis[idx]:
                cnt[idx] -= 1
                if cnt[idx] == 0: tot -= 1
            tail += 1

        return res

    ### 77. Combinations ###
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        if n < k or k <= 0: return [[]]
        if n == k: return [range(1,n+1)]
        return self.combine(n-1,k) + [x+[n] for x in self.combine(n-1, k-1)]

    ### 78. Subsets ###
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if not nums: return [[]]

        nums.sort()
        l = len(nums)
        def dfs(cur):
            if cur == l: return [[]]
            a = dfs(cur+1)
            return a + [[nums[cur]]+x for x in a]

        return dfs(0)

    ### 79. Word Search ###
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        m, n, l = len(board), len(board[0]), len(word)
        cnt = [0] * 130
        for i in board:
            for j in i:
                cnt[ord(j)] += 1
        for x in word:
            cnt[ord(x)] -= 1
            if cnt[ord(x)] < 0: return False

        move = [[-1,0],[0,1],[1,0],[0,-1]]
        vis = [[False] * n for _ in xrange(m)]

        def dfs(x, y, cur):
            if board[x][y] != word[cur]: return False
            if cur == l-1: return True
            vis[x][y] = True

            for d in move:
                tx, ty = x+d[0], y+d[1]
                if tx < 0 or ty < 0 or tx >= m or ty >= n: continue
                if not vis[tx][ty] and dfs(tx, ty, cur+1): return True

            vis[x][y] = False
            return False

        for i in xrange(m):
            for j in xrange(n):
                if dfs(i,j,0): return True
        return False
