class Solution:
    ### 140. Word Break II ###
    # @param s, a string
    # @param wordDict, a set<string>
    # @return
    def wordBreak(self, s, wordDict):
        l = len(s)
        dp = [[] for i in xrange(l+1)]
        dp[0].append([])
        for i in xrange(l):
            for w in wordDict:
                lw = len(w)
                if s[:i+1].endswith(w) and dp[i+1-lw]:
                    dp[i+1].append(w)

        def dfs(pos):
            res = []
            for p in dp[pos]:
                lp = len(p)
                if lp == pos: res.append(p)
                else:
                    res.extend([(x + ' ' + p) for x in dfs(pos-lp)])
            return res

        return dfs(l)

    ### 141. Linked List Cycle ###
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head or not head.next: return False

        one = two = head
        flag = False
        while one and two:
            one = one.next
            two = two.next and two.next.next
            if one == two:
                flag = True
                break

        return flag

    ### 142. Linked List Cycle II ###
    # @param head, a listNode
    # @return a list node
    def detectCycle(self, head):
        if not head or not head.next: return None

        one = two = head
        flag = False
        while one and two:
            one = one.next
            two = two.next and two.next.next
            if one == two:
                flag = True
                break

        if not flag: return None
        three = head
        while three != one:
            one = one.next
            three = three.next

        return one

    ### 143. Reorder List ###
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        le, cur= 0, head
        while cur:
            cur=cur.next
            le += 1

        if le <= 2: return

        h, l, pre = (le-1)/2, head, None
        while h:
            tmp = l.next
            l.next = pre
            pre = l
            l = tmp
            h -= 1

        cur = l
        l = pre
        if le & 1:
            r = cur.next
            cur.next = None
        else:
            r = cur.next.next
            cur.next.next = None
        while l and r:
            tmp = r.next
            r.next = cur
            cur = r
            r = tmp

            tmp = l.next
            l.next = cur
            cur = l
            l = tmp

    ### 144. Binary Tree Preorder Traversal ###
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        if not root: return []

        order = []
        stack = [root]
        while stack:
            cur = stack.pop()
            order.append(cur.val)
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)

        return order

    ### 145. Binary Tree Postorder Traversal ###
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        if not root: return []

        order = []
        stack = [root]
        while stack:
            cur = stack.pop()
            order.append(cur.val)
            if cur.left: stack.append(cur.left)
            if cur.right: stack.append(cur.right)

        return order[::-1]

    ### 147. Insertion Sort List ###
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head
        cur = head.next
        tail = head
        head.next = None
        while cur:
            find = dummy
            nxt = cur.next
            if tail.val <= cur.val:
                tail.next = cur
                tail = tail.next
                tail.next = None
            else:
                while find.next:
                    if find.next.val >= cur.val:
                        cur.next = find.next
                        find.next = cur
                        break
                    find = find.next
            cur = nxt

        return dummy.next

    ### 148. Sort List ###
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head or not head.next:
            return head

        if head.val <= head.next.val: l, r = head, head.next
        else: l, r = head.next, head

        tl, tr = l, r
        mid = r
        cur = head.next.next
        l.next = r.next = None
        while cur:
            if cur.val < mid.val:
                tl.next = cur
                tl = tl.next
                cur = cur.next
            elif cur.val > mid.val:
                tr.next = cur
                tr = tr.next
                cur = cur.next
            else:
                tmp = cur.next
                cur.next = r.next
                r.next = cur
                if r == tr: tr = tr.next
                r = r.next
                cur = tmp

        tmp = r.next
        tl.next = None
        tr.next = None
        r.next = None
        l = self.sortList(l)
        p = self.sortList(tmp)

        head = l
        while l.next: l=l.next
        l.next = mid
        r.next = p

        return head

    ### 149. Max Points on a Line ###
    # @param {Point[]} points
    # return {integer}
    def maxPoints(self, points):
        cnt = 0
        l = len(points)
        for i in xrange(l):
            record = {}
            left, same = 0, 1
            for j in xrange(i+1, l):
                dx = 1.0 * (points[i].x-points[j].x)
                dy = 1.0 * (points[i].y-points[j].y)
                if dx == 0 and dy == 0:
                    same += 1
                    continue

                if (dx == 0): idx = 'oo'
                else: idx = int(dy / dx * 1000000)
                if record.get(idx): record[idx] += 1
                else: record[idx] = 1

                left = max(left, record[idx])
            del record
            cnt = max(cnt, left+same)

        return cnt
