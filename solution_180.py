class Solution:
    # 187.
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        l = len(s)
        record = {}
        for i in xrange(0, l-9):
            ss = s[i:i+10]
            if record.has_key(ss): record[ss] += 1
            else: record[ss] = 1

        ans = []
        for k, v in record.items():
            if v > 1: ans.append(k)

        return ans

    # 199
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        if not prices: return 0
        l = len(prices)
        if k >= l/2:
            return sum([prices[i+1] - prices[i]  for i in xrange(l-1) if prices[i+1] - prices[i] > 0])

        dp1 = [0] * (k+1)
        dp2 = [0] * (k+1)
        for i in xrange(1,l):
            diff = prices[i] - prices[i-1]
            for j in xrange(k,0,-1):
                dp1[j] = max(dp2[j-1]+diff, dp1[j]+diff)
                dp2[j] = max(dp2[j], dp1[j])

        return dp2[k]


    # 189.
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place
    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    # 190.
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #NOTE: 'format' function
        # < : Left align(default)
        # > : Right align
        # ^ : Middle align
        # = : Decimal point align(for decimal only)
        #return int('{:0>32b}'.format(n)[::-1], 2)
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)

        return n

    # 191
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        cnt = 0
        while n:
            if n & 1: cnt += 1
            n >>= 1

        return cnt

    # 198
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        n = len(nums)
        if not n: return 0

        left = 0
        taken = nums[0]
        for i in xrange(1, n):
            tmp_left = max(left, taken)
            tmp_taken = left + nums[i]

            left = tmp_left
            taken = tmp_taken

        return max(left, taken)

    # 199
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if not root: return []

        layer, ans = [], []
        layer.append(root)
        ans.append(root.val)
        while True:
            tmp = []
            for node in layer:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)

            if not tmp: break
            ans.append(tmp[-1].val)
            del layer
            layer = tmp
            del tmp

        return ans

    # 200
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid: return 0

        move = [[-1,0],[0,1],[1,0],[0,-1]]
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        vis = [[False for j in xrange(n)] for i in xrange(m)]
        def dfs(x, y):
            vis[x][y] = True
            for i in move:
                tx = x+i[0]
                ty = y+i[1]
                if tx >= 0 and tx < m and ty >= 0 and ty < n and not vis[tx][ty] and grid[tx][ty] == '1':
                    dfs(tx, ty)

        for i in xrange(m):
            for j in xrange(n):
                if vis[i][j] == False and grid[i][j] == '1':
                    dfs(i,j)
                    cnt += 1

        return cnt

    # 201
    # @param m, an integer
    # @param n, an integer
    # return an integer
    def rangeBitwiseAnd(self, m, n):
        if m == n: return m

        mm = self.reverseBits(m)
        nn = self.reverseBits(n)
        kk = (mm ^ nn) & (-(mm ^ nn))
        k  = ~((self.reverseBits(kk) << 1) - 1)

        return m & n & k

    # 202
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        calc = lambda a: sum([int(i)**2 for i in str(a)])
        vis = set()
        while n not in vis:
            vis.add(n)
            n = calc(n)

        return n == 1

    # 203
    # @pararm {ListNode} head
    # @pararm {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        pre = ListNode(None)
        pre.next = head
        dummy = pre
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
            head = head.next

        return dummy.next

    # 204
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2: return 0

        is_prime = [True for i in xrange(n)]
        prime = [2]
        cnt = 1
        for i in xrange(3, n, 2):
            if is_prime[i]:
                prime.append(i)
                cnt += 1
            for j in xrange(len(prime)):
                if i * prime[j] >= n: break
                is_prime[i * prime[j]] = False

        return cnt

    # 205
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        mapping = {}
        for i in xrange(len(s)):
            if not mapping.get(s[i]): mapping[s[i]] = t[i]
            elif mapping[s[i]] != t[i]: return False

        return len(mapping) == len(set(mapping.values()))

    # 206
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head or not head.next: return head

        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre

    # 207
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequistes):
        edge = [[] for i in xrange(numCourses)]
        indegree = [0] * numCourses
        vis = [False] * numCourses
        for p in prerequistes:
            edge[p[1]].append(p[0])
            indegree[p[0]] += 1

        def dfs(st):
            vis[st] = True
            for v in edge[st]:
                indegree[v] -= 1
                if not indegree[v]:
                    dfs(v)

        for i in xrange(numCourses):
            if not indegree[i] and not vis[i]:
                dfs(i)
        flag = True
        for i in indegree:
            if i:
                flag = False
                break

        return flag

    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        l = len(nums)
        res = None
        head = tail = cur = 0
        while head < l:
            while tail < l and cur < s:
                cur += nums[tail]
                tail += 1
            if cur < s: break
            if not res or tail-head < res: res = tail-head
            cur -= nums[head]
            head += 1

        return res or 0
