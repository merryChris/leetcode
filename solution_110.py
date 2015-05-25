class Solution:
    # 110
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root: return True

        def internalCheck(r):
            if not r: return (True, 0)
            if not r.left and not r.right: return (True, 1)

            ls = internalCheck(r.left)
            rs = internalCheck(r.right)
            dc = max(ls[1], rs[1])+1
            if not ls[0] or not rs[0]: return (False, dc)
            if abs(ls[1]-rs[1]) > 1: return (False, dc)

            return (True, dc)

        return internalCheck(root)[0]

    # 111
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1

        ld = rd = None
        if root.left: ld = self.minDepth(root.left)
        if root.right: rd = self.minDepth(root.right)
        if ld and rd: return min(ld, rd)+1
        return (ld or rd) + 1

    # 112
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root: return False
        if not root.left and not root.right:
            return root.val == sum

        if root.left and self.hasPathSum(root.left, sum-root.val): return True
        if root.right and self.hasPathSum(root.right, sum-root.val): return True

        return False

    # 113
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        if not root: return []
        paths = []

        def dfs(r, s, p):
            if not r.left and not r.right:
                if r.val == s: paths.append(p+[r.val])
                return
            if r.left: dfs(r.left, s-r.val, p+[r.val])
            if r.right: dfs(r.right, s-r.val, p+[r.val])

        dfs(root, sum, [])
        return paths

    # 114
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        if not root: return
        can = []

        def dfs(r):
            can.append(r)
            if r.left: dfs(r.left)
            if r.right: dfs(r.right)

        dfs(root)
        for i in xrange(len(can)-1):
            can[i].left = None
            can[i].right = can[i+1]
        can[-1].left = can[-1].right = None

        return

    # 115
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        ls, lt = len(s), len(t)
        dp = [1] + [0] * lt
        for i in xrange(1,ls+1):
            for j in xrange(lt,0,-1):
                if s[i-1] == t[j-1]: dp[j] += dp[j-1]

        return dp[lt]

    # 116, 117
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return

        last = [root]
        while last:
            cur = []
            pre = None
            for x in last:
                if x.left:
                    cur.append(x.left)
                    if pre: pre.next = x.left
                    pre = x.left
                if x.right:
                    cur.append(x.right)
                    if pre: pre.next = x.right
                    pre = x.right
            last = cur
            del cur


    # 118
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        rows = []
        if numRows == 0: return rows
        rows.append([1])
        if numRows == 1: return rows

        for t in xrange(1,numRows):
            tmp = [1]
            for x in xrange(1,t): tmp.append(rows[t-1][x-1]+rows[t-1][x])
            tmp.append(1)
            rows.append(tmp)

        return rows

    # 119
    # @param {interger} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        pre = [1]
        for t in xrange(1,rowIndex+1):
            cur = [1]
            for x in xrange(1,t): cur.append(pre[x-1]+pre[x])
            cur.append(1)
            pre = cur

        return cur
