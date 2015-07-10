class Solution:
    ### 30. Substring with Concatenation of All Words ###
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if not s or not words or len(s) < len(words[0]): return []

        l, record, res = len(words[0]), {}, []
        for w in words:
            if not record.has_key(w): record[w] = 0
            record[w] += 1
        for _ in xrange(l):
            cnt = record.copy()
            head = tail = _
            while tail+l <= len(s):
                while tail+l <= len(s):
                    cur = s[tail:tail+l]
                    if not cnt.has_key(cur) or cnt[cur] == 0: break
                    cnt[cur] -= 1
                    tail += l
                if tail - head == l * len(words): res.append(head)
                while head < tail:
                    tmp = s[head:head+l]
                    cnt[tmp] += 1
                    head += l
                    if tmp == cur: break
                if not cnt.has_key(cur):
                    head += l
                    tail += l

        return res

    ### 31. Next Permutation ###
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead
    def nextPermutation(self, nums):
        if not nums: return

        head = None
        for i in xrange(len(nums)-1):
            if nums[i] < nums[i+1]: head = i
        if head is None: nums.sort()
        else:
            pos, aim = head, len(nums)
            head += 1
            tail = len(nums)-1
            while head <= tail:
                nums[head], nums[tail] = nums[tail], nums[head]
                if nums[head] > nums[pos] and head < aim: aim = head
                if nums[tail] > nums[pos] and tail < aim: aim = tail
                head += 1
                tail -= 1
            nums[pos], nums[aim] = nums[aim], nums[pos]

        return

    ### 32. Longest Valid Parentheses ###
    # @param {string} s
    # @param {integer}
    def longestValidParentheses(self, s):
        if not s: return 0

        cnt = 0
        dp = [0] * len(s)
        for i in xrange(len(s)):
            c = s[i]
            if c == '(': cnt += 1
            elif cnt > 0:
                cnt -= 1
                dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2]

        return max(dp)

    ### 33. Search in Rotated Sorted Array ###
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums: return -1

        def dfs(l, r, n):
            if nums[l] == n: return l
            if nums[r] == n: return r
            if l >= r-1: return -1

            mid = (l+r) >> 1
            if n > nums[l]:
                if nums[mid] > nums[l] and nums[mid] < n: return dfs((l+r+1)>>1, r, n)
                return dfs(l, mid, n)
            else:
                if nums[mid] < nums[l] and nums[mid] >= n: return dfs(l, mid, n)
                return dfs((l+r+1)>>1, r, n)

        return dfs(0, len(nums)-1, target)

    ### 34. Search for a Range ###
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if not nums or target < nums[0] or target > nums[-1]: return [-1, -1]

        ll = rr = -1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] >= target: r=mid-1
            else: l=mid+1
        if nums[l] == target: ll = l

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] > target: r=mid-1
            else: l=mid+1
        if nums[r] == target: rr=r

        return [ll, rr]

    ### 35. Search Insert Position ###
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if not nums or target < nums[0]: return 0
        if target > nums[-1]: return len(nums)

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] >= target: r=mid-1
            else: l=mid+1

        return l

    ### 36. Valid Sudoku ###
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        if not board: return True

        for i in xrange(9):
            valid = [False] * 10
            for j in xrange(9):
                if board[i][j] == '.': continue
                idx = int(board[i][j])
                if idx < 1 or idx > 9: return False
                if not valid[idx]: valid[idx] = True
                else: return False

            valid = [False] * 10
            for j in xrange(9):
                if board[j][i] == '.': continue
                idx = int(board[j][i])
                if idx < 1 or idx > 9: return False
                if not valid[idx]: valid[idx] = True
                else: return False

            valid = [False] * 10
            for j in xrange(9):
                if board[i/3*3+j/3][i%3*3+j%3] == '.': continue
                idx = int(board[i/3*3+j/3][i%3*3+j%3])
                if idx < 1 or idx > 9: return False
                if not valid[idx]: valid[idx] = True
                else: return False

        return True

    ### 37. Sudoku Solver ###
    # @param {character[][]}
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        if not board: return

        dots = []
        row = [[False] * 9 for _ in xrange(9)]
        col = [[False] * 9 for _ in xrange(9)]
        squ = [[False] * 9 for _ in xrange(9)]
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    dots.insert(0, (i,j))
                else:
                    idx = int(board[i][j])
                    row[i][idx-1] = True
                    col[j][idx-1] = True
                    squ[i/3*3+j/3][idx-1] = True

        def dfs():
            if not dots: return True

            i,j = dots.pop()
            for n in xrange(9):
                if not row[i][n] and not col[j][n] and not squ[i/3*3+j/3][n]:
                    row[i][n] = True
                    col[j][n] = True
                    squ[i/3*3+j/3][n] = True
                    board[i][j] = str(n+1)
                    if dfs(): return True
                    row[i][n] = False
                    col[j][n] = False
                    squ[i/3*3+j/3][n] = False
                    board[i][j] = '.'
            dots.append((i,j))
            return False

        dfs()
        return

    ### 38. Count and Say ###
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n < 1: return ''

        res = '1'
        for _ in xrange(n-1):
            tmp, pre, cnt = '', None, 0
            for x in res+'#':
                if pre and x != pre:
                    tmp += str(cnt) + pre
                    cnt = 1
                else: cnt += 1
                pre = x
            res = tmp

        return res

    ### 39. Combination Sum ###
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        if not candidates: return [[]]

        candidates = sorted(list(set(candidates)))
        res = []
        def dfs(left, cur, fr):
            if not left and cur:
                res.append(cur)
                return
            if fr == len(candidates): return

            for i in xrange((left+candidates[fr])//candidates[fr]):
                dfs(left-candidates[fr]*i, cur+[candidates[fr]]*i, fr+1)
            return

        dfs(target, [], 0)
        return res
