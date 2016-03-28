class Solution:
    ### 210. Course Schedule II ###
    # @param {integer} n
    # @parame {integer[][]} prerequisites
    # @return {integer}
    def findOrder(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        edges = []
        for _ in xrange(numCourses): edges.append([])
        for cur, pre in prerequisites:
            indegree[cur] += 1
            edges[pre].append(cur)

        queue, res = [], []
        for _ in xrange(numCourses):
            if not indegree[_]: queue.append(_)
        while queue:
            u = queue.pop(0)
            for v in edges[u]:
                indegree[v] -= 1
                if not indegree[v]: queue.append(v)
            res.append(u)

        if len(res) != numCourses: res = []
        return res

    ### 212. Word Search II ###
    # @param {character[][]} board
    # @param {string} words
    # @return {string[]}
    def findWords(self, board, words):
        if not board: return []

        from solution_class import Trie
        tree = Trie()
        for i in range(len(words)): tree.insert(words[i], i)

        m, n, res = len(board), len(board[0]), []
        grid = [[ord(board[i][j])-97 for j in range(n)] for i in range(m)]

        def dfs(x, y, root):
            idx = grid[x][y]
            if not root.chd[idx]: return
            root = root.chd[idx]
            if root.bj != -1:
                res.append(root.bj)
                root.bj = -1

            grid[x][y] = None
            for dx, dy in ((-1,0), (0,1), (1,0), (0,-1)):
                tx, ty = x+dx, y+dy
                if 0 <= tx < m and 0 <= ty < n and grid[tx][ty] != None:
                    dfs(tx, ty, root)
            grid[x][y] = idx

        for i in range(m):
            for j in range(n):
                dfs(i, j, tree.root)

        return [words[i] for i in res]

    ### 213. House Robber II ###
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0: return 0
        if len(nums) <= 3: return max(nums)

        def internal_rob(nums):
            left, taken = 0, nums[0]
            for num in nums[1:]:
                left, taken = max(left, taken), left+num

            return left, taken

        return max(internal_rob(nums)[0], max(internal_rob(nums[1:])))

    ### 214. Shortest Palindrome ###
    # @param {string} str
    # @return {string}
    def shortestPalindrome(self, s):
        if not s: return ''

        ss = '\001'.join(['']+list(s)+[''])
        dp = [0] * len(ss)
        pivot = right = bj = -1
        for i in xrange(len(ss)):
            r = 1
            if right >= i:
                r = max(r, min(dp[pivot*2-i], right-i+1))
            while i-r+1>=0 and i+r-1<len(ss) and ss[i-r+1] == ss[i+r-1]:
                r += 1
            r -= 1
            dp[i] = r
            if i+r > right:
                right = i+r
                pivot = i
            if dp[i] == i+1:
                bj = i

        return s[bj:][::-1] + s

    ### 215. Kth Largest Element in an Array ###
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        cur = nums[0]
        i, j = 1, len(nums)-1
        while i <= j:
            while i < len(nums) and nums[i] <= cur: i += 1
            while j > 0 and nums[j] >= cur: j -= 1
            if i < j: nums[i], nums[j] = nums[j], nums[i]

        fr, to = len(nums)-i+1, len(nums)-j
        if k >= fr and k <= to: return cur
        elif k < fr: return self.findKthLargest(nums[i:], k)
        return self.findKthLargest(nums[1:j+1], k-to)

    ### 216. Combination Sum III ###
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if n == 0: return []

        res = []
        def dfs(cnt, num, fr, cur):
            if cnt == 0 and num == 0:
                res.append(cur)
            if cnt == 0 or fr > 9 or fr > num: return

            for i in xrange(fr, 10):
                if i <= num: dfs(cnt-1, num-i, i+1, cur+[i])

        dfs(k, n, 1, [])
        return res

    ### 217. Contains Duplicate ###
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

    ### 218. The Skyline Problem ###
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        if not buildings: return []

        endpoints, cnt = [], {}
        for bd in buildings:
            endpoints.append((bd[0], bd[2], 1))
            endpoints.append((bd[1], bd[2], -1))
            cnt[bd[2]] = 0
        def internal_cmp(x, y):
            if x[0] != y[0]: return cmp(x[0], y[0])
            if x[2] != y[2]: return cmp(y[2], x[2])
            if x[2] == 1: return cmp(y[1], x[1])
            return cmp(x[1], y[1])

        endpoints.sort(cmp=lambda x, y: internal_cmp(x,y))

        cur, rec, res = -1, set(), []
        for ep in endpoints:
            if ep[1] != cur:
                if ep[1] > cur:
                    cur = ep[1]
                    res.append([ep[0], ep[1]])
                cnt[ep[1]] += ep[2]
                if cnt[ep[1]] == 0: rec.remove(ep[1])
                elif cnt[ep[1]] == 1: rec.add(ep[1])
            else:
                cnt[cur] += ep[2]
                if cnt[cur] == 0:
                    rec.remove(cur)
                    cur = max(rec) if len(rec) else 0
                    res.append([ep[0], cur])

        return res

    ### 219. Contains Duplicate II ###
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if not nums or k <= 0: return False

        record = set()
        for i in xrange(len(nums)):
            if nums[i] in record: return True
            if i-k >= 0: record.remove(nums[i-k])
            record.add(nums[i])

        return False
