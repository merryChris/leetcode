class Solution:
    ### 310. Minimum Height Trees ###
    # @param {integer} n
    # @param {integer[][]} edges
    # @return {integer[]}
    def findMinHeightTrees(self, n, edges):
        if not n: return []

        deg, rec = [0]*n, {}
        for e in edges:
            deg[e[0]] += 1
            deg[e[1]] += 1
            if e[0] not in rec: rec[e[0]] = []
            if e[1] not in rec: rec[e[1]] = []
            rec[e[0]].append(e[1])
            rec[e[1]].append(e[0])
        res, cur, cnt = [i for i in range(n) if deg[i]<=1], [], 0
        while cnt < n-2:
            cur, res = res, []
            cnt += len(cur)
            for i in cur:
                for j in rec[i]:
                    deg[j] -= 1
                    if deg[j] == 1: res.append(j)

        return res

    ### 312. Burst Balloons ###
    # @param {integer[]} nums
    # @return {integer}
    def maxCoins(self, nums):
        if not nums: return 0

        dp = [[-1]*(len(nums)-i) for i in xrange(len(nums))]
        def dfs(i, j, l, r):
            if j < i: return 0
            if dp[i][j-i] != -1: return dp[i][j-i]

            dp[i][j-i] = max([l*r*nums[p] + dfs(i,p-1,l,nums[p]) + dfs(p+1,j,nums[p],r) for p in xrange(i,j+1)])
            return dp[i][j-i]

        return dfs(0, len(nums)-1, 1, 1)

    ### 313. Super Ugly Number ###
    # @param {integer} n
    # @param {integer[]} primes
    # @return {integer}
    def nthSuperUglyNumber(self, n, primes):
        if n <= 0: return 0

        dp, idx = [1], [0]*len(primes)
        rec = [(primes[i]*dp[idx[i]], i) for i in range(len(primes))]
        import heapq
        heapq.heapify(rec)
        while len(dp) < n:
            min_val, min_idx = heapq.heappop(rec)
            if dp[-1] != min_val: dp.append(min_val)
            idx[min_idx] += 1
            heapq.heappush(rec, (primes[min_idx]*dp[idx[min_idx]], min_idx))

        return dp[-1]

    ### 315. Count of Smaller Numbers After Self  ###
    # @param {integer[]} nums
    # @return {integer}
    def countSmaller(self, nums):
        if not nums: return []

        n, res = len(nums), []
        c, sorted_nums = [0]*(n+1), sorted(nums)
        def bis(val):
            l, r = 0, n-1
            while l<=r:
                mid = (l+r)>>1
                if sorted_nums[mid] >= val: r=mid-1
                else: l=mid+1
            return l+1

        def bit_update(pos):
            while pos <= n:
                c[pos] += 1
                pos += pos&(-pos)

        def bit_sum(pos):
            res = 0
            while pos > 0:
                res += c[pos]
                pos -= pos&(-pos)
            return res

        for val in nums[::-1]:
            pos = bis(val)
            res.append(bit_sum(pos-1))
            bit_update(pos)

        return res[::-1]

    ### 316. Remove Duplicate Letters ###
    # @param {string} s
    # @return {string}
    def removeDuplicateLetters(self, s):
        if not s: return ''

        last, instack, stack = {s[i]: i for i in xrange(len(s))}, 0, []
        for i in xrange(len(s)):
            idx = ord(s[i])-97
            if (1 << idx) & instack: continue
            while stack and stack[-1] > s[i] and last[stack[-1]] > i:
                instack ^= 1 << (ord(stack.pop())-97)
            stack.append(s[i])
            instack |= (1 << idx)

        return ''.join(stack)

    ### 318. Maximum Product of Word Lengths ###
    # @param {string[]} words
    # @return {integer}
    def maxProduct(self, words):
        if not words: return 0

        hash_val = []
        for w in words:
            val = 0
            for c in set(w):
                val |= 1 << (ord(c)-97)
            hash_val.append(val)
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if hash_val[i] & hash_val[j] == 0:
                    res = max(res, len(words[i])*len(words[j]))

        return res

    ### 319. Bulb Switcher ###
    # @param {integer} n
    # @return {integer}
    def bulbSwitch(self, n):
        import math
        return int(math.sqrt(n))
