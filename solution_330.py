class Solution:
    ### 330. Patching Array ###
    # @param {integer[]} nums
    # @param {integer} n
    # @return {integer}
    def minPatches(self, nums, n):
        if not n: return 0

        cur, cnt = 0, 0
        nums.append(n+1)
        for x in nums:
            while cur < x-1 and cur < n:
                cur += cur+1
                cnt += 1
            if cur >= n: break
            cur += x

        return cnt

    ### 331. Verify Preorder Serialization of a Binary Tree ###
    # @param {string} preorder
    # @return {boolean}
    def isValidSerialization(self, preorder):
        if not preorder: return False

        capacity = 1
        for cur in preorder.split(','):
            capacity -= 1
            if capacity < 0: break
            if cur != '#': capacity += 2

        return capacity == 0

    ### 332. Reconstruct Itinerary ###
    # @param {string[][]} tickets
    # @return {string[]}
    def findItinerary(self, tickets):
        if not tickets: return []

        edges, res = {}, []
        for t in tickets:
            if t[0] not in edges: edges[t[0]] = {}
            if t[1] not in edges[t[0]]: edges[t[0]][t[1]] = 0
            edges[t[0]][t[1]] += 1

        def dfs(cur):
            if cur in edges:
                for c in sorted(edges[cur].keys()):
                    if edges[cur][c] > 0:
                        edges[cur][c] -= 1
                        dfs(c)
            res.append(cur)

        dfs('JFK')
        return res[::-1]

    ### 334. Increasing Triplet Subsequence ###
    # @param {integer[]} nums
    # @return {boolean}
    def increasingTriplet(self, nums):
        if not nums or len(nums)<3: return False

        fir, sec, flag = None, None, False
        for x in nums:
            if fir is None: fir = x
            elif sec is None:
                if x < fir: fir = x
                elif x > fir: sec = x
            elif fir < x < sec: sec = x
            elif fir > x: fir = x
            elif sec < x: flag = True; break

        return flag

    ### 335. Self Crossing ###
    # @param {integer[]} x
    # @return {boolean}
    def isSelfCrossing(self, x):
        if not x: return False
        if len(x) < 4 and x.count(0) > 0: return False

        for i in range(3, len(x)):
            if x[i] == 0: return True
            if x[i-1] <= x[i-3] and x[i] >= x[i-2]: return True
            if i >= 4 and x[i-1] == x[i-3] and x[i]+x[i-4] >= x[i-2]: return True
            if i >= 5 and x[i-1] < x[i-3] and x[i-2] >= x[i-4] and x[i]+x[i-4] >= x[i-2] and \
               x[i-1]+x[i-5] >= x[i-3]: return True

        return False

    # 336. Palindrome Pairs ###
    # @param {string[]} words
    # @return {integer[][]}
    def palindromePairs(self, words):
        if not words: return []

        loc, rec, res = {words[i]:i for i in range(len(words))}, {}, []
        def check(s):
            if len(s) <= 1: return True
            if s in rec: return rec[s]
            l, r, flag = 0, len(s)-1, True
            while l <= r:
                if s[l] != s[r]:
                    flag = False
                    break
                l += 1
                r -= 1
            rec[s] = flag
            return flag

        for i in range(len(words)):
            lw = len(words[i])
            tmp = words[i][::-1]
            if tmp in loc and loc[tmp] != i: res.append([i, loc[tmp]])
            for j in range(lw):
                tmp = words[i][:j][::-1]
                if tmp in loc and check(words[i][j:]): res.append([i, loc[tmp]])
                tmp = words[i][lw-j:][::-1]
                if tmp in loc and check(words[i][:lw-j]): res.append([loc[tmp], i])

        return res

    # 337. House Robber III ###
    # @param {TreeNode} root
    # @return {integer}
    def rob(self, root):
        if not root: return 0

        dp = ({}, {})
        def dfs(r, rob):
            if not r: return 0
            if not r.left and not r.right:
                return r.val if rob else 0
            if r in dp[rob]: return dp[rob][r]

            res = dfs(r.left, 0)+dfs(r.right, 0)
            if rob == 0: res = max(res, dfs(r.left,1)+dfs(r.right,0), dfs(r.left,0)+dfs(r.right,1), \
                                   dfs(r.left,1)+dfs(r.right,1))
            if rob == 1: res += r.val
            dp[rob][r] = res
            return res

        return max(dfs(root,0), dfs(root,1))

    # 338. Counting Bits ###
    # @param {integer} num
    # @return {integer[]}
    def countBits(self, num):
        if num <= 0: return [0]

        dp = [0]
        for x in range(1, num+1):
            dp.append(dp[x>>1])
            if x&1: dp[-1] += 1

        return dp
