class Solution:
    ### 90. Subsets II ###
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        subsets = []
        nums.sort()
        l = len(nums)
        def dfs(idx, sub):
            subsets.append(sub)
            if idx < l: dfs(idx+1, sub + [nums[idx]])
            for i in xrange(idx+1, l):
                if nums[i] == nums[i-1]: continue
                dfs(i+1, sub + [nums[i]])

        dfs(0, [])
        return subsets

    ### 91. Decode Ways ###
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s: return 0

        l = len(s)
        dp = [1]
        for i in xrange(l):
            res = 0
            if s[i] != '0': res += dp[-1]
            if i>=1 and str(int(s[i-1:i+1])) == s[i-1:i+1] and int(s[i-1:i+1]) <= 26:
                res += dp[-2]
            if res == 0: return 0
            dp.append(res)

        print dp
        return dp[-1]

    ### 92. Reverse Linked List II ###
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        begin = end = head
        cnt = 1
        while cnt < m:
            pre = begin
            begin = begin.next
            end = end.next
            cnt += 1
        while cnt < n:
            end = end.next
            cnt += 1
        tail = end.next
        while begin != end:
            tmp = begin.next
            begin.next = tail
            tail = begin
            begin = tmp
        end.next = tail
        pre.next = end

        return dummy.next

    ### 93. Restore IP Addresses ###
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        l = len(s)
        ip = []

        def check(addr):
            return int(addr) <= 255 and str(int(addr)) == addr

        def dfs(idx, nums):
            if len(nums) == 3:
                if idx < l and check(s[idx:]): ip.append('.'.join(nums+[s[idx:]]))
            else:
                for i in xrange(idx+1, l):
                    if check(s[idx:i]):
                        dfs(i, nums+[s[idx:i]])

        dfs(0, [])
        return ip

    ### 94. Binary Tree Inorder Traversal ###
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        if not root: return []

        order = []
        stack = [[root, 0]]
        while stack:
            cur = stack[-1]
            if cur[1] == 0:
                cur[1] = 1
                if cur[0].left:
                    stack.append([cur[0].left, 0])
            else:
                order.append(cur[0].val)
                stack.pop()
                if cur[0].right:
                     stack.append([cur[0].right, 0])

        return order

    ### 95. Unique Binary Search Trees II ###
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        if n <= 0: return [[]]

        dp = []
        for i in xrange(n):
            dp.append([])
            for j in xrange(n):
                dp[i].append([])

        def dfs(fr, to):
            if fr > to: return [None]
            if dp[fr-1][to-1]: return dp[fr-1][to-1]

            nodeList = []
            for x in xrange(fr, to+1):
                l = dfs(fr,x-1)
                r = dfs(x+1,to)
                for ll in l:
                    for rr in r:
                        root = TreeNode(x)
                        root.left = ll
                        root.right = rr
                        nodeList.append(root)

            dp[fr-1][to-1] = nodeList
            return nodeList

        return dfs(1,n)

    ### 96. Unique Binary Search Trees ###
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        if n <= 1: return n
        dp = [1] + [0] * n
        for i in xrange(1,n+1):
            for j in xrange(i):
                dp[i] += dp[j] * dp[i-j-1]

        return dp[n]

    ### 97. Interleaving String ###
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1+l2 != l3: return False
        for x in set(s3):
            if s1.count(x) + s2.count(x) != s3.count(x):
                return False

        dp1 = []
        dp2 = []
        for x in xrange(l3+1):
            dp1.append([False] * (l1+1))
            dp2.append([False] * (l2+1))
        dp1[0][0] = dp2[0][0] = True
        for i in xrange(1,l3+1):
            for j in xrange(1,min(i,l1)+1):
                dp1[i][j] = s1[j-1] == s3[i-1] and (dp1[i-1][j-1] or (i-j <= l2 and dp2[i-1][i-j]))
            for j in xrange(1,min(i,l2)+1):
                dp2[i][j] = s2[j-1] == s3[i-1] and (dp2[i-1][j-1] or (i-j <= l1 and dp1[i-1][i-j]))

        return dp1[l3][l1] or dp2[l3][l2]

    ### 98. Validate Binary Search Tree ###
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        if not root: return True

        cur, pre = root, None
        while cur:
            if not cur.left:
                if pre and pre.val >= cur.val:
                    return False
                pre = cur
                cur = cur.right
            else:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = cur
                    cur = cur.left
                else:
                    tmp.right = None
                    if pre and pre.val >= cur.val:
                        return False
                    pre = cur
                    cur = cur.right

        return True

    ### 99. Recover Binary Search Tree ###
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        if not root: return

        fir = sec = None
        cur, pre = root, None
        while cur:
            if not cur.left:
                if pre and pre.val > cur.val:
                    if not fir: fir, sec = pre, cur
                    else: sec = cur
                pre = cur
                cur = cur.right
            else:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = cur
                    cur = cur.left
                else:
                    tmp.right = None
                    if pre and pre.val > cur.val:
                        if not fir: fir, sec = pre, cur
                        else: sec = cur
                    pre = cur
                    cur = cur.right
        if fir and sec:
            tmp = fir.val
            fir.val = sec.val
            sec.val = tmp

        return
