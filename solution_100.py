class Solution:
    # 100
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q: return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 101
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root: return True

        def dfs(left, right):
            if not left and not right: return True
            if not left or not right: return False

            return left.val == right.val and dfs(left.right, right.left) and dfs(left.left, right.right)

        return dfs(root.left, root.right)

    # 102
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root: return []

        order = []
        queue = [(root, 0)]
        level = -1
        while queue:
            cur = queue.pop(0)
            if cur[1] > level:
                order.append([])
                level += 1

            order[cur[1]].append(cur[0].val)
            if cur[0].left: queue.append((cur[0].left, cur[1]+1))
            if cur[0].right: queue.append((cur[0].right, cur[1]+1))

        return order

    # 103
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if not root: return []

        order = []
        queue = [(root, 0)]
        level = -1
        while queue:
            cur = queue.pop(0)
            if cur[1] > level:
                order.append([])
                level += 1

            if cur[1] & 1: order[cur[1]].insert(0, cur[0].val)
            else: order[cur[1]].append(cur[0].val)
            if cur[0].left: queue.append((cur[0].left, cur[1]+1))
            if cur[0].right: queue.append((cur[0].right, cur[1]+1))

        return order

    # 104
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # 105
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTreeI(self, preorder, inorder):
        if not preorder or not inorder: return None

        val = preorder.pop(0)
        pos = inorder.index(val)
        root = TreeNode(val)
        root.left = self.buildTreeI(preorder, inorder[:pos])
        root.right = self.buildTreeI(preorder, inorder[pos+1:])

        return root

    # 106
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder: return None

        val = postorder.pop()
        pos = inorder.index(val)
        root = TreeNode(val)
        root.right = self.buildTree(inorder[pos+1:], postorder)
        root.left = self.buildTree(inorder[:pos], postorder)

        return root

    # 107
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if not root: return []

        order = []
        queue = [(root, 0)]
        level = -1
        while queue:
            cur = queue.pop(0)
            if cur[1] > level:
                order.append([])
                level += 1

            order[cur[1]].append(cur[0].val)
            if cur[0].left: queue.append((cur[0].left, cur[1]+1))
            if cur[0].right: queue.append((cur[0].right, cur[1]+1))

        return order[::-1]


    # 108
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if not nums: return None

        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

    # 109
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if not head: return None
        can = []
        cur = head
        l = 0
        while cur:
            can.append(cur)
            l += 1
            cur = cur.next

        def internalTransfer(l, r):
            if l == r: return None
            if l+1 == r: return TreeNode(can[l].val)

            mid = (l+r) / 2
            root = TreeNode(can[mid].val)
            root.left = internalTransfer(l,mid)
            root.right = internalTransfer(mid+1, r)

            return root

        return internalTransfer(0, l)
