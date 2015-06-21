class Solution:
    ### 50. Pow(x, n) ###
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        unit, res = x, 1.0
        flag = False if n<0 else True
        n = abs(n)
        while n:
            if n & 1: res *= unit
            unit *= unit
            n >>= 1

        return res if flag else 1.0/res

    ### 51. N-Queens ###
    # @param {integer} n
    # @return a list of lists of string
    def solveNQueens(self, n):
        if n == 0: return []

        board, row, upper = [], [], (1<<n)-1
        def dfs(r, ld, rd):
            if r == upper:
                puzzle = '.'*n
                board.append([puzzle[:x]+'Q'+puzzle[x+1:] for x in row])
                return
            st = ~(r|ld|rd)&upper
            for i in xrange(n):
                cur = 1 << i
                if st & cur:
                    row.append(i)
                    dfs(r+cur, (ld+cur)<<1, (rd+cur)>>1)
                    row.pop()

            return

        dfs(0,0,0)
        return board

    ### 52. N-Queens II ###
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        if n == 0: return []

        upper = (1<<n)-1
        def dfs(r, ld, rd):
            if r == upper: return 1

            st = ~(r|ld|rd)&upper
            cnt = 0
            while st:
                cur = st & (-st)
                cnt += dfs(r+cur, (ld+cur)<<1, (rd+cur)>>1)
                st -= cur

            return cnt

        return dfs(0,0,0)

    ### 53. Maximum Subarray ###
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if not nums: return 0

        n, val = len(nums), nums[0]
        dp = [0] * n
        for i in xrange(n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            val = max(val, dp[i])

        return val

    ### 54. Spiral Matrix ###
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix: return []

        m, n = len(matrix), len(matrix[0])
        def check(loc):
            return loc[0] >= 0 and loc[1] >= 0 and loc[0] < m and loc[1] < n

        move = ((0,1),(1,0),(0,-1),(-1,0))
        vis = [[False]*n for _ in xrange(m)]
        order, cur, d, cnt = [], (0,-1), 0, 0
        while cnt < m*n:
            nxt = (cur[0]+move[d][0], cur[1]+move[d][1])
            if check(nxt) and not vis[nxt[0]][nxt[1]]:
                cur = nxt
                order.append(matrix[cur[0]][cur[1]])
                vis[cur[0]][cur[1]] = True
                cnt += 1
            else: d = (d+1)%4

        return order

    ### 55. Jump Game ###
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if not nums: return True

        l, left = len(nums), 1
        for x in nums:
            left -= 1
            if left < 0: break
            left = max(left, x)

        return left >= 0

    ### 56. Merge Intervals ###
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        intervals.sort(key=lambda x:(x.end, x.start))
        new = []
        while intervals:
            cur = intervals.pop()
            while intervals:
                if intervals[-1].end < cur.start: break
                tmp = intervals.pop()
                cur.start = min(cur.start, tmp.start)
                cur.end = max(cur.end, tmp.end)
            new.append(cur)

        return new[::-1]

    ### 57. Insert Interval ###
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]

        le = len(intervals)
        l, r = 0, le-1
        while l <= r:
            mid = (l+r)>>1
            if intervals[mid].start > newInterval.start: r=mid-1
            else: l=mid+1
        pos = 0 if r == -1 else r
        if pos < le and intervals[pos].end < newInterval.start: pos += 1
        if pos == le: return intervals + [newInterval]
        while pos < le:
            if intervals[pos].start > newInterval.end:
                intervals.insert(pos, newInterval)
                break
            tmp = intervals.pop(pos)
            newInterval.start = min(newInterval.start, tmp.start)
            newInterval.end = max(newInterval.end, tmp.end)
            le -= 1
        if pos == le: intervals.append(newInterval)

        return intervals

    ### 58. Length of Last Word ###
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if not s.strip(): return 0
        return len(s.split()[-1])

    ### 59. Spiral Matrix II ###
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n <= 0: return []
        if n == 1: return [[1]]

        def check(loc):
            return loc[0] >= 0 and loc[1] >= 0 and loc[0] < n and loc[1] < n

        move = ((0,1),(1,0),(0,-1),(-1,0))
        grid, cur, d, num = [[0]*n for _ in xrange(n)], (0,0), 0, 1
        while True:
            grid[cur[0]][cur[1]] = num
            if num == n*n: break
            nxt = (cur[0]+move[d][0], cur[1]+move[d][1])
            if check(nxt) and grid[nxt[0]][nxt[1]] == 0:
                cur = nxt
                num += 1
            else: d = (d+1)%4

        return grid
