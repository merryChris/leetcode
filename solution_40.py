class Solution:
    ### 40. Combination Sum II ###
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        if not candidates: return [[]]

        candidates.sort()
        res = []
        def dfs(left, cur, fr):
            if not left and cur:
                res.append(cur)
                return
            if fr == len(candidates): return

            pos = fr+1
            while pos < len(candidates) and candidates[pos] == candidates[fr]: pos += 1
            dfs(left, cur, pos)
            if left >= candidates[fr]: dfs(left-candidates[fr], cur+[candidates[fr]], fr+1)
            return

        dfs(target, [], 0)
        return res

    ### 41. First Missing Positive ###
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        if not nums: return 1

        l = len(nums)
        for i in xrange(l):
            while nums[i] > 0 and nums[i] < l and i+1 != nums[i] and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in xrange(l):
            if i+1 != nums[i]: return i+1

        return l+1

    ### 42. Trapping Rain Water ###
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        l = len(height)
        if not height or l == 1: return 0

        left, right = [-1]*l, [-1]*l
        for i in xrange(1,l):
            left[i] = max(left[i-1], height[i-1])
            right[l-i-1] = max(right[l-i], height[l-i])

        return sum([max(min(left[_], right[_])-height[_], 0) for _ in xrange(l)])

    ### 43. Multiply Strings ###
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        return str(long(num1)*long(num2))

    ### 44. Wildcard Matching ###
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not s: return len(p) == p.count('*')
        if len(p) - p.count('*') > len(s): return False

        dp, cur = [False] * len(s), 0
        for x in p:
            flag = False
            if x == '*':
                flag = True
                for i in xrange(cur, len(s)):
                    dp[i] = True
            else:
                for i in xrange(len(s)-1,cur-1,-1):
                    if (s[i] == x or x == '?') and (i == 0 or dp[i-1]):
                        flag = True
                        dp[i] = True
                        cur = i+1
                    else: dp[i] = False
            if not flag: return False

        return dp[-1]

    ### 45. Jump Game II ###
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        if not nums: return -1

        l = len(nums)
        step = cur = last = farest = 0
        while farest < l:
            while cur <= last:
                farest = max(farest, cur+nums[cur])
                cur += 1
            if last == l-1: break
            if last == farest: return -1
            last = farest
            step += 1

        return step

    ### 46. Permutations ###
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if not nums: return []
        res, cur, l = [], [], len(nums)

        def dfs(nums):
            if len(cur) == l:
                res.append([_ for _ in cur])
                return

            for i in xrange(len(nums)):
                cur.append(nums[i])
                dfs(nums[:i]+nums[i+1:])
                cur.pop()

        nums.sort()
        dfs(nums)
        return res

    ### 47. Permutations II ###
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        if not nums: return []
        res, cur, l = [], [], len(nums)

        def dfs(nums):
            if len(cur) == l:
                res.append([_ for _ in cur])
                return

            for i in xrange(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    cur.append(nums[i])
                    dfs(nums[:i]+nums[i+1:])
                    cur.pop()

        nums.sort()
        dfs(nums)
        return res

    ### 48. Rotate Image ###
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        m, n = 0, len(matrix)
        while m < n//2:
            for i in xrange(m,n-m-1):
                tmp = matrix[m][i]
                matrix[m][i] = matrix[n-i-1][m]
                matrix[n-i-1][m] = matrix[n-m-1][n-i-1]
                matrix[n-m-1][n-i-1] = matrix[i][n-m-1]
                matrix[i][n-m-1] = tmp
            m += 1

        return

    ### 49. Anagrams ###
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        if not strs: return []

        groups, record = [], {}
        for x in strs:
            key = ''.join(sorted(x))
            if key not in record: record[key] = []
            record[key].append(x)

        for g in record.values():
            if len(g)>1: groups.extend(g)

        return groups
