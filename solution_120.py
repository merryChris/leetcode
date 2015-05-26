class Solution:
    ### 120. Triangle ###
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        t = len(triangle)
        for i in xrange(0,t-1):
            pre = triangle[i][0]
            l = len(triangle[i])
            for j in xrange(l):
                triangle[i+1][j] += min(pre, triangle[i][j])
                pre = triangle[i][j]
            triangle[i+1][l] += pre

        return min(triangle[t-1])

    ### 121. Best Time to Buy and Sell Stock ###
    # @param {integer[]} prices
    # @return {integer}
    def maxProfitI(self, prices):
        if not prices: return 0

        profit, preMin = 0, prices[0]
        for p in prices[1:]:
            preMin = min(preMin, p)
            profit = max(profit, p - preMin)

        return profit

    ### 122. Best Time to Buy and Sell Stock II ###
    # @param {integer[]} prices
    # @param {integer}
    def maxProfitII(self, prices):
        if not prices: return 0
        return sum([prices[i+1] - prices[i]  for i in xrange(len(prices)-1) if prices[i+1] - prices[i] > 0])

    ### 123. Best Time to Buy and Sell Stock III ###
    # @param {integer[]} prices
    # @param {integer}
    def maxProfit(self, prices):
        if not prices: return 0

        l = len(prices)
        dp = [0] * l
        preMin = prices[0]
        for i in xrange(1,l):
            dp[i] = max(dp[i-1], prices[i] - preMin)
            preMin = min(preMin, prices[i])

        res = dp[l-1]
        postMax = prices[-1]
        for i in xrange(l-2,0,-1):
            res = max(res, dp[i] + postMax - prices[i+1])
            postMax = max(postMax, prices[i])

        return res

    ### 124. Binary Tree Maximum Path Sum ###
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        if not root: return 0

        dp = []
        idx = 0
        def dfs(c):
            l = r = 0
            if c.left: l = max(l, dfs(c.left))
            if c.right: r = max(r, dfs(c.right))

            dp.append(l + r + c.val)
            return max(l, r) + c.val

        dfs(root)
        return reduce(lambda x, y: max(x, y) ,dp, dp[0])

    ### 125. Valid Palindrome ###
    # @param {string s}
    # @param {boolean}
    def isPalindrome(self, s):
        s = filter(str.isalnum, str(s)).lower()
        return s == s[::-1]

    ### 126. Word Ladder II ###
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        queue = [(start,1)]
        path = {start: []}
        vis = {start: 1}
        alphabet = 'qwertyuioplkjhgfdsazxcvbnm'
        dict.add(end)
        l = len(start)
        while queue:
            cur = queue.pop(0)
            for i in xrange(l):
                for j in alphabet:
                    if cur[0][i] == j: continue
                    w = cur[0][:i] + j + cur[0][i+1:]
                    if w in dict:
                        if not vis.get(w):
                            vis[w] = cur[1]+1
                            path[w] = []
                            if w != end: queue.append((w, cur[1]+1))
                        if vis.get(w) == cur[1]+1:
                            path[w].append(cur[0])

        def dfs(s, e):
            if s == e: return [[s]]
            if not path.get(e): return []

            col = []
            for w in path[e]:
                col.extend([x + [e] for x in dfs(s,w)])
            return col

        return dfs(start, end)

    ### 127. Word Ladder ###
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, s set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        queue = [(beginWord,1,0), (endWord,1,1)]
        vis = {beginWord: (1,0), endWord: (1,1)}
        l = len(beginWord)
        alphabet = 'qwertyuioplkjhgfdsazxcvbnm'
        while queue:
            cur = queue.pop(0)
            for i in xrange(l):
                for j in alphabet:
                    if cur[0][i] == j: continue
                    w = cur[0][:i] + j + cur[0][i+1:]
                    if w in wordDict:
                        if not vis.get(w):
                            vis[w] = (cur[1]+1, cur[2])
                            queue.append((w, cur[1]+1, cur[2]))
                        elif vis.get(w)[1] != cur[2]:
                            return cur[1] + vis.get(w)[0]

        return 0

    ### 128. Longest Consecutive Sequence ###
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        record = {}
        con = 1
        for x in nums:
            if record.get(x): continue
            l = record.get(x-1) or 0
            r = record.get(x+1) or 0
            record[x] = record[x-l] = record[x+r] = l+r+1
            con = max(con, l+r+1)

        return con

    ### 129. Sum Root to Leaf Numbers ###
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        def dfs(r, val, tot):
            if not r: return None

            val *= 10
            val += r.val
            lv = dfs(r.left, val, tot)
            rv = dfs(r.right, val, tot)

            if lv is None and rv is None:
                tot += val

            if lv: tot += lv
            if rv: tot += rv

            return tot

        return dfs(root, 0, 0) or 0
