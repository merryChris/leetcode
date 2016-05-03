class Solution:
    ### 273. Integer to English Words ###
    # @param {integer} num
    # @return {string}
    def numberToWords(self, num):
        if num == 0: return 'Zero'

        less20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', \
                  'Twelve','Thirteen','Fourteen','Fifteen','Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']

        def dfs(num, pos=0):
            if not num: return ''

            res = []
            if num>999: res.append(dfs(num/1000, pos+1))
            if num>999 and num/1000%1000>0: res.append(thousands[pos+1])
            num %= 1000
            if num>99 and num/100>0: res.extend([less20[num/100], 'Hundred'])
            if num>9:
                last2 = num%100
                if 0<last2<20: res.append(less20[last2])
                if last2>=20 and last2/10>0: res.append(tens[last2/10])
                if last2>=20 and last2%10>0: res.append(less20[last2%10])
            if 0<num<10: res.append(less20[num])
            return ' '.join(map(str, res))

        return dfs(num)

    ### 274. H-Index ###
    # @param {integer[]} citations
    # @return {integer}
    def hIndex(self, citations):
        if not citations: return 0

        cnt, tot, res = [0] * (len(citations)+1), 0, 0
        for x in citations:
            cnt[min(x, len(citations))] += 1
        for i in xrange(len(citations),-1,-1):
            tot += cnt[i]
            if tot >= i:
                res = i
                break

        return res

    ### 275. H-Index II ###
    # @param {integer[]} citations
    # @return {integer}
    def hIndex(self, citations):
        if not citations: return 0

        l, r = 0, len(citations)
        while l <= r:
            mid = (l+r)>>1
            if citations[-mid] >= mid: l = mid+1
            else: r = mid-1

        return r

    ### 278. First Bad Version ###
    # @param {integer} n
    # @return {integer}
    def firstBadVersion(self, n):
        if not n: return 0

        l, r = 1, n
        while l <= r:
            mid = (l+r)>>1
            if isBadVersion(mid): r = mid-1
            else: l = mid+1

        return l

    ### 279. Perfect Squares ###
    # @param {integer} n
    # @return {integer}
    numSquaresDP = [0]
    def numSquares(self, n):
        if not n: return 0
        if n < len(self.numSquaresDP): return self.numSquaresDP[n]

        for i in range(len(self.numSquaresDP), n+1):
            res, cur = i, 1
            while cur**2 <= i:
                res = min(res, self.numSquaresDP[i-cur**2]+1)
                cur += 1
            self.numSquaresDP.append(res)

        return self.numSquaresDP[n]

    ### 282. Expression Add Operators ###
    # @param {string} num
    # @param {integer} target
    # @return {integer[]}
    def addOperators(self, num, target):
        if not num: return []

        def make(pos, vs, vc, si, path, res):
            cur = 0
            for i in range(pos, len(num)):
                cur = cur*10+int(num[i])
                if '+' in si: dfs(i+1, vs+vc,  cur, path+'+'+num[pos:i+1], res)
                if '-' in si: dfs(i+1, vs+vc, -cur, path+'-'+num[pos:i+1], res)
                if '*' in si: dfs(i+1, vs,  vc*cur, path+'*'+num[pos:i+1], res)
                if cur == 0: break

        def dfs(pos, vs, vc, path, res):
            if pos == len(num):
                if vs+vc == target: res.append(path[1:])
            else: make(pos, vs, vc, '+-*', path, res)

        res  = []
        make(0, 0, 0, '+', '', res)
        return res

    ### 283. Move Zeroes ###
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def moveZeroes(self, nums):
        if not nums: return []

        pos = 0
        for i in xrange(len(nums)):
            if nums[i] == 0: continue
            nums[pos] = nums[i]
            pos += 1

        nums[pos:] = [0]*(len(nums)-pos)

    ### 287. Find the Duplicate Number ###
    # @param {integer[]} nums
    # @return {integer}
    def findDuplicate(self, nums):
        if not nums: return None

        #NOTE: SINCE ZERO IS NOT INCLUDED IN ARRAY.
        slow, fast, finder = 0, 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder: break

        return finder

    ### 289. Game of Life ###
    # @param {integer[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def gameOfLife(self, board):
        if not board or not board[0]: return

        m, n = len(board), len(board[0])
        move = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
        def count(x, y):
            cnt = 0
            for d in move:
                tx, ty = x+d[0], y+d[1]
                if 0<=tx<m and 0<=ty<n: cnt += board[tx][ty]%2
            return cnt

        for i in range(m):
            for j in range(n):
                cnt = count(i,j)
                if board[i][j] == 0 and cnt == 3: board[i][j] = 2
                if board[i][j] == 1 and cnt not in (2,3): board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                elif board[i][j] == 3: board[i][j] = 0
