class Solution:
    ### 321. Create Maximum Number ###
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @param {integer} k
    # @return {integer[]}
    def maxNumber(self, nums1, nums2, k):
        if not k or len(nums1)+len(nums2)<k: return []

        loc1 = [[-1]*10 for _ in range(len(nums1)+1)]
        loc2 = [[-1]*10 for _ in range(len(nums2)+1)]
        l12 = len(nums1)+len(nums2)
        vis, res = set(), [-1]*k

        def make(nums, loc):
            pos = [-1]*10
            for i in xrange(len(nums)-1,-1,-1):
                pos[nums[i]] = i
                for j in range(10):
                    loc[i][j] = pos[j]

        def compare(p1, p2):
            if p2 == len(nums2): return 1
            if p1 == len(nums1): return 2
            if nums1[p1] > nums2[p2]: return 1
            if nums1[p1] < nums2[p2]: return 2
            return compare(p1+1, p2+1)

        def dfs(p1, p2, k):
            if k == 0 or (p1, p2, k) in vis: return

            if l12 == p1+p2+k:
                flag, update = True, False
                while flag and k>0:
                    if compare(p1, p2) == 1:
                        if res[-k] <= nums1[p1] or update:
                            if res[-k] < nums1[p1]: update = True
                            res[-k] = nums1[p1]
                            p1 += 1
                        else: flag = False
                    else:
                        if res[-k] <= nums2[p2] or update:
                            if res[-k] < nums2[p2]: update = True
                            res[-k] = nums2[p2]
                            p2 += 1
                        else: flag = False
                    k -= 1
            else:
                flag = False
                for i in range(9,-1,-1):
                    if loc1[p1][i] != -1:
                        if l12-loc1[p1][i]-p2 >= k and res[-k] <= i:
                            if res[-k] < i: res[-k:] = [-1]*k
                            res[-k] = i
                            dfs(loc1[p1][i]+1, p2, k-1)
                            flag = True
                    if loc2[p2][i] != -1:
                        if l12-p1-loc2[p2][i] >= k and res[-k] <= i:
                            if res[-k] < i: res[-k:] = [-1]*k
                            res[-k] = i
                            dfs(p1, loc2[p2][i]+1, k-1)
                            flag = True
                    if flag: break
            vis.add((p1, p2, k))

        make(nums1, loc1)
        make(nums2, loc2)
        dfs(0, 0, k)
        return res

    ### 322. Coin Change ###
    # @param {integer[]} coins
    # @param {integer} amount
    # @return {integer}
    def coinChange(self, coins, amount):
        if not amount: return 0

        coins.sort(reverse=True)
        self.res = amount+1
        def dfs(st, left, cnt):
            if not left:
                self.res = min(self.res, cnt)
                return
            for i in xrange(st, len(coins)):
                if left >= coins[i]*(self.res-cnt): break
                if left%coins[i] == 0:
                    self.res = min(self.res, cnt+left/coins[i])
                    break
                if coins[i] <= left: dfs(i, left-coins[i], cnt+1)

        dfs(0, amount, 0)
        return self.res if self.res != amount+1 else -1

    ### 324. Wiggle Sort II ###
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def wiggleSort(self, nums):
        if not nums: return

        def getKthElement(l, r, k):
            if l == r: return nums[l]
            pivot = nums[l]
            ll, rr = l, r
            while l <= r:
                while l<=rr and nums[l] <= pivot: l+=1
                while ll<r  and nums[r] >= pivot: r-=1
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1; r -= 1
            if k < r-ll: return getKthElement(ll+1, r, k)
            elif k >= l-ll: return getKthElement(l, rr, k-l+ll)
            return pivot


        def index(i):
            return (i<<1|1) % (len(nums)|1)

        median = getKthElement(0, len(nums)-1, len(nums)//2)
        left, mid, right = 0, 0, len(nums)-1
        while mid <= right:
            if nums[index(mid)] > median:
                nums[index(left)], nums[index(mid)] = nums[index(mid)], nums[index(left)]
                left += 1; mid += 1
            elif nums[index(mid)] < median:
                nums[index(right)], nums[index(mid)] = nums[index(mid)], nums[index(right)]
                right -= 1
            else:
                mid += 1

    ### 326. Power of Three ###
    # @param {integer} n
    # @return {boolean}
    def isPowerOfThree(self, n):
        if n <= 0: return False
        while not n%3: n/=3
        return n == 1

    ### 327. Count of Range Sum ###
    # @param {integer[]} nums
    # @param {integer} lower
    # @param {integer} upper
    # @return {integer}
    def countRangeSum(self, nums, lower, upper):
        if not nums: return 0

        cur, rec = 0, set([0])
        for i in range(len(nums)):
            cur += nums[i]
            rec.add(cur)
        s = sorted(rec)
        c, cur, cnt = [0]*(len(s)+1), 0, 0

        def bit_update(pos):
            while pos<=len(s):
                c[pos] += 1
                pos += pos&(-pos)

        def bit_sum(pos):
            res = 0
            while pos>0:
                res += c[pos]
                pos -= pos&(-pos)
            return res

        import bisect
        bit_update(bisect.bisect_right(s, 0))
        for i in range(len(nums)):
            cur += nums[i]
            cnt += bit_sum(bisect.bisect_right(s, cur-lower))
            cnt -= bit_sum(bisect.bisect_left(s, cur-upper))
            bit_update(bisect.bisect_right(s, cur))

        return cnt

    ### 328. Odd Even Linked List ###
    # param {ListNode} head
    # return {ListNode}
    def oddEvenList(self, head):
        if not head or not head.next: return head

        odd, even, dhead = head, head.next, head.next
        while True:
            if not even.next: break
            odd.next = even.next
            odd = odd.next

            if not odd.next: break
            even.next = odd.next
            even = even.next

        odd.next = dhead
        even.next = None

        return head

    ### 329. Longest Increasing Path in a Matrix ###
    # @param {integer[][]} matrix
    # @return integer
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]: return 0

        m, n, res = len(matrix), len(matrix[0]), 0
        dp = [[-1]*n for _ in range(m)]
        move = ((-1,0),(0,1),(1,0),(0,-1))

        def dfs(x, y):
            if dp[x][y] != -1: return dp[x][y]

            dp[x][y] = 1
            for d in move:
                tx, ty = x+d[0], y+d[1]
                if 0<=tx<m and 0<=ty<n and matrix[x][y] < matrix[tx][ty]:
                    dp[x][y] = max(dp[x][y], dfs(tx, ty)+1)
            return dp[x][y]

        for i in xrange(m):
            for j in xrange(n):
                res = max(res, dfs(i, j))

        return res
