class Solution:
    ### 240. Search a 2D Matrix II ###
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix: return False

        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while 0<=i<m and 0<=j<n:
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: i-=1
            else: j+=1

        return False

    ### 241. Different Ways to Add Parentheses ###
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        if not input: return []

        res = []
        for i in xrange(len(input)):
            if input[i] in '+-*':
                for x in self.diffWaysToCompute(input[:i]):
                    for y in self.diffWaysToCompute(input[i+1:]):
                        if input[i] == '+': res.append(x+y)
                        if input[i] == '-': res.append(x-y)
                        if input[i] == '*': res.append(x*y)
        if not res: res.append(int(input))

        return res

    ### 242. Valid Anagram ###
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if not s and not t: return True

        cnt = {}
        for x in s:
            if x in cnt: cnt[x] += 1
            else: cnt[x] = 1
        for x in t:
            if x in cnt and cnt[x]: cnt[x] -= 1
            else: return False
        for _, v in cnt.items():
            if v > 0: return False

        return True

    ### 257. Binary Tree Paths ###
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]

        return [str(root.val)+'->'+x for x in self.binaryTreePaths(root.left)+self.binaryTreePaths(root.right)]

    ### 258. Add Digits ###
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        if not num: return 0
        if num % 9 == 0: return 9
        return num % 9

    ### 260. Single Number III ###
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        if not nums: return []
        if len(nums) <= 2: return nums

        xor = reduce(int.__xor__, nums)
        lastBit, le, ri = xor & (-xor), 0, 0
        for x in nums:
            if x & lastBit: le ^= x
            else: ri ^= x

        return [le, ri]

    ### 263. Ugly Number ###
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        if num <= 0: return False
        if num < 7: return True

        while num%2 == 0: num /= 2
        while num%3 == 0: num /= 3
        while num%5 == 0: num /= 5

        return num == 1

    ### 264, Ugly Number II ###
    # @param {integer} n
    # @return {integer}
    def nthUglyNumber(self, n):
        if n <= 0: return 0

        dp, i2, i3, i5 = [1], 0, 0, 0
        for _ in range(n-1):
            c2, c3, c5 = dp[i2]*2, dp[i3]*3, dp[i5]*5
            res = min(c2, c3, c5)
            dp.append(res)
            if res == c2: i2 += 1
            if res == c3: i3 += 1
            if res == c5: i5 += 1

        return dp[-1]

    ### 268. Missing Number ###
    # @param {integer[]} nums
    # @return {integer}
    def missingNumber(self, nums):
        if not nums: return 0
        return len(nums)*(len(nums)+1)/2-sum(nums)
