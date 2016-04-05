class Solution:
    ### 230. Kth Smallest Element in a BST ###
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        if not root: return None

        def dfs(root, k):
            cl, cr, le, ri = 0, 0, None, None
            if root.left: cl, le = dfs(root.left, k)
            if le: return cl, le
            if cl+1 == k: return k, root
            if root.right: cr, ri = dfs(root.right, k-cl-1)
            return cl+1+cr, ri

        return dfs(root, k)[-1].val

    ### 231. Power of Two ###
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n and not (n & (n-1)) and True or False

    ### 233. Number of Digit One ###
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        if n <= 0: return 0

        wei, m = 0, n
        while m:
            wei += 1
            m /= 10
        dp = [0] * (wei+1)
        for i in xrange(1,wei+1):
            dp[i] = dp[i-1]*10 + 10**(i-1)

        def dfs(num, pos):
            if pos == 0: return 0

            jin = 10**(pos-1)
            cur = num/jin%10
            res = dp[pos-1] * cur
            if cur > 1: res += jin
            elif cur == 1: res += num%jin+1
            return res+dfs(num%jin, pos-1)

        return dfs(n, wei)

    ### 234. Palindrome Linked List ###
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head or not head.next: return True

        cnt, cur = 0, head
        while cur:
            cnt += 1
            cur = cur.next
        pre, h1, h2 = None, None, head
        for _ in xrange(cnt//2):
            pre = h1
            h1 = h2
            h2 = h1.next
            h1.next = pre
        if cnt & 1: h2 = h2.next
        while h1 and h2:
            if h1.val != h2.val: return False
            h1 = h1.next
            h2 = h2.next

        return True

    ### 235. Lowest Common Ancestor of a Binary Search Tree ###
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        if min(p.val, q.val) > root.val: return self.lowestCommonAncestor(root.right, p, q)
        if max(p.val, q.val) < root.val: return self.lowestCommonAncestor(root.left, p, q)
        return root

    ### 236. Lowest Common Ancestor of a Binary Tree ###
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None

        def dfs(root, p, q):
            cl, cr, cc, le, ri = 0, 0, 0, None, None
            if root.left: cl, le = dfs(root.left, p, q)
            if cl == 2: return cl, le
            if root.right: cr, ri = dfs(root.right, p, q)
            if cr == 2: return cr, ri
            if root == p or root == q: cc = 1
            if cl+cr+cc == 2: return 2, root
            return cl+cr+cc, None

        return dfs(root, p, q)[-1]

    ### 237. Delete Node in a Linked List ###
    # @param {ListNode} node
    # @return {void} Do not return anything, modify matrix in-place instead.
    def deleteNode(self, node):
        if not node: return

        node.val = node.next.val
        node.next = node.next.next

    ### 238. Product of Array Except Self ###
    # @param {integer[]} nums
    # @return [integer[]]
    def productExceptSelf(self, nums):
        if not nums: return []

        l, r, res = 1, 1, [1]*len(nums)
        for i in xrange(len(nums)-1):
            l *= nums[i]
            r *= nums[len(nums)-i-1]
            res[i+1] *= l
            res[len(nums)-i-2] *= r

        return res

    ### 239. Sliding Window Maximum ###
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        if not nums or len(nums) < k: return []

        stack, res, head = [], [], 0
        for i in xrange(len(nums)):
            while stack and head<len(stack) and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])
            if i >= k:
                while head<len(stack) and stack[head] <= nums[i-k]:
                    head += 1
                    if stack[head-1] == nums[i-k]: break
            if i>=k-1: res.append(stack[head])

        return res
