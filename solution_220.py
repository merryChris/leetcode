class Solution:
    ### 220. Contains Duplicate III ###
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not nums or k<=0 or t<0: return False

        record, l = {}, len(nums)
        for i in xrange(l):
            bucket = nums[i] // (t+1)
            for key in (bucket-1, bucket, bucket+1):
                if key in record and abs(record.get(key)-nums[i]) <= t:
                    return True
            if i-k >= 0: record.pop(nums[i-k] // (t+1))
            record[bucket] = nums[i]

        return False

    ### 221. Maximal Square ###
    # @param {integer[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix: return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in xrange(m)]
        for i in xrange(m): dp[i][0] = 1 if matrix[i][0] == '1' else 0
        for i in xrange(n): dp[0][i] = 1 if matrix[0][i] == '1' else 0
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

        res = 0
        for i in xrange(m):
            res = max(res, max(dp[i]))

        return res*res

    ### 222. Count Complete Tree Nodes ###
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        def dfs(r):
            h = 0
            while r:
                h += 1
                r = r.left
            return h

        cnt = 0
        while root:
            lh, rh = dfs(root.left), dfs(root.right)
            cnt += 2 ** rh
            if lh == rh: root = root.right
            else: root = root.left

        return cnt

    ### 223. Rectangle Area ###
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        res = (C-A)*(D-B)+(G-E)*(H-F)
        I = max(A, E)
        J = max(B, F)
        K = min(C, G)
        L = min(D, H)
        if I < K and J < L: res -= (K-I)*(L-J)

        return res

    ### 224. Basic Calculator ###
    ### 227. Basic Calculator II ###
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        if not s: return 0

        def check(x, y):
            if x == '(': return False
            if y == ')': return True
            if x in '+-' and y in '*/': return False
            return True

        sign, num, cur = ['('], [], ''
        for c in s+')':
            if c.isspace(): continue
            elif c.isdigit(): cur+=c
            else:
                if cur: num.append(int(cur))
                cur = ''
                if c == '(': sign.append(c)
                else:
                    while sign and check(sign[-1], c):
                        a, b, x, v = num.pop(), num.pop(), sign.pop(), 0
                        if x == '+': v = a+b
                        if x == '-': v = b-a
                        if x == '*': v = a*b
                        if x == '/': v = b/a
                        num.append(v)
                    if sign and c == ')': sign.pop()
                    else: sign.append(c)

        return num.pop()

    ### 226. Invert Binary Tree ###
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root: return None

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root

    ### 228. Summary Ranges ###
    # @param {integer[]} nums
    # @return {integer[]}
    def summaryRanges(self, nums):
        if not nums: return []

        res, bj = [], 0
        for i in range(len(nums)+1):
            if i == len(nums) or nums[i]-nums[bj] != i-bj:
                if bj == i-1: res.append(str(nums[bj]))
                else: res.append(str(nums[bj])+'->'+str(nums[i-1]))
                bj = i

        return res

    ### 229. Majority Element II ###
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        a = b = None
        ca = cb = 0
        for x in nums:
            if x == a: ca += 1
            elif x == b: cb += 1
            elif a == None:
                a = x
                ca = 1
            elif b == None:
                b = x
                cb = 1
            else:
                ca -= 1
                if ca == 0: a = None
                cb -= 1
                if cb == 0: b = None
        res = []
        ca = cb = 0
        for x in nums:
            if a != None and a == x: ca += 1
            if b != None and b == x: cb += 1
        if a != None and ca > len(nums)//3: res.append(a)
        if b != None and cb > len(nums)//3: res.append(b)

        return res
