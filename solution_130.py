class Solution:
    ### 130. Surrounded Regions ###
    # @param {charactar[][]} board
    # @return {void} Do not return anythin, modify board in-place instead.
    def solve(self, board):
        if not board: return

        move = [[-1,0], [0,1], [1,0], [0,-1]]
        board[:] = [list(x) for x in board]
        m = len(board)
        n = len(board[0])

        def bfs(x, y):
            board[x][y] = '#'
            queue = []
            queue.append((x,y))
            while queue:
                cur = queue.pop(0)
                for k in move:
                    tx, ty = cur[0]+k[0], cur[1]+k[1]
                    if tx >= 0 and tx < m and ty >= 0 and ty < n:
                        if board[tx][ty] == 'O':
                            board[tx][ty] = '#'
                            queue.append((tx, ty))

        for i in xrange(m):
            for j in [0,n-1]:
                if board[i][j] == 'O':
                    bfs(i,j)
        for i in [0,m-1]:
            for j in xrange(n):
                if board[i][j] == 'O':
                    bfs(i,j)
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == '#': board[i][j] = 'O'
                elif board[i][j] == 'O': board[i][j] = 'X'

        board[:] = [''.join(x) for x in board]
        return

    ### 131. Palindrome Partitioning ###
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        if not s: return [[]]

        can = []
        for i in xrange(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                can.extend([[s[:i+1]]+x for x in self.partition(s[i+1:])])

        return can

    ### 132. Palindrome Partitioning II ##
    # abcdcbaabcdc 2
    # @param {string} s
    # @oaram {integer}
    def minCut(self, s):
        if s == s[::-1]: return 0

        palin = []
        l = len(s)
        for i in xrange(l): palin.append([True]*l)

        for i in xrange(1,l):
            for j in xrange(l-i):
                palin[j][j+i] = palin[j+1][j+i-1] and  (s[j] == s[j+i])

        dp = [0] * l
        for i in xrange(1,l):
            if palin[0][i]:
                dp[i] = 0
                continue
            tmp = dp[i-1] + 1
            for j in xrange(i-1):
                if palin[j+1][i]:
                    tmp = min(tmp, dp[j]+1)
            dp[i] = tmp

        return dp[l-1]

    ### 133. Clone Graph ###
    # @param {a undirected graph node} node
    # @return {a undirected graph node}
    def cloneGraph(self, node):
        if not node: return None

        head = UndirectedGraphNode(node.label)
        queue = [node]
        record = {}
        record[node] = head

        while queue:
            cur = queue.pop(0)
            tmp = record[cur]

            for c in cur.neighbors:
                nc = record.get(c, None) or UndirectedGraphNode(c.label)
                tmp.neighbors.append(nc)
                if c not in record:
                    record[c] = nc
                    queue.append(c)

        return head

    ### 134. Gas Station ###
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        l = len(gas)
        cur = 0
        while cur<l:
            pos = cur
            bj = cur
            cnt = 0
            while True:
                if cnt + gas[cur] < cost[cur]:
                    break
                cnt = cnt + gas[cur] - cost[cur]
                cur = (cur + 1) % l
                if cur == pos: return pos
            if cur < bj: break
            cur += 1

        return -1

    ### 135. Candy ###
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        l = len(ratings)
        cnt = [1]*l
        for i in xrange(1,l):
            if ratings[i] > ratings[i-1]:
                cnt[i] = cnt[i-1]+1
        for i in xrange(l-1,0,-1):
            if ratings[i] < ratings[i-1]:
                cnt[i-1] = max(cnt[i-1], cnt[i]+1)

        return sum(cnt)

    ### 136. Single Number ###
    # @param {integer[]} nums
    # @return {integer}
    def singleNumberI(self, nums):
        return reduce(int.__xor__, nums)

    ### 137. Single Number II  ###
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        high = low = 0
        for x in nums:
            high += low & x
            low ^= x
            mod = high & low
            high ^= mod
            low ^= mod

        return (high << 1) + low

    ### 138. Copy List with Random Pointer ###
    # @param {a RandomListNode} head
    # @return {a RandomListNode}
    def copyRandomList(self, head):
        if not head: return None

        dummy = {}
        cur = head
        while cur:
            dummy[cur] = RandomListNode(cur.label)
            cur = cur.next
        cur = head
        while cur:
            dummy[cur].next = dummy.get(cur.next)
            dummy[cur].random = dummy.get(cur.random)
            cur = cur.next

        return dummy.get(head)

    ### 139. Word Break ###
    # @param {string} s
    # @param {set<string>} wordDict
    # @return {boolean}
    #def wordBreak(self, s, wordDict):
    def wordBreakI(self, s, wordDict):
        l = len(s)
        dp = [True] + [False]*l
        for i in xrange(l):
            for w in wordDict:
                lw = len(w)
                if s[:i+1].endswith(w) and dp[i+1-lw]:
                    dp[i+1] = True
                    break

        return dp[l]
