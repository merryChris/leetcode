class Solution:
    ### 10. Regular Expression Matching ###
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not s: return len(p) == p.count('*')*2
        if len(p) - p.count('*')*2 > len(s): return False

        dp, cur, skip = [False] * len(s), len(s)-1, False
        for _ in xrange(len(p)-1, -1, -1):
            if skip:
                skip = False
                continue
            flag = False
            if p[_] == '*':
                flag = True
                skip = True
                for i in xrange(cur, -1, -1):
                    if (s[i] == p[_-1] or p[_-1] == '.') and (i == len(s)-1 or dp[i+1]): dp[i] = True
            else:
                for i in xrange(cur+1):
                    if (s[i] == p[_] or p[_] == '.') and (i == len(s)-1 or dp[i+1]):
                        flag = True
                        dp[i] = True
                        cur = i-1
                    else: dp[i] = False
            if not flag: return False

        return dp[0]

    ### 11. Container With Most Water ###
    # @param {integer[]} height
    # @return  {integer}
    def maxArea(self, height):
        if not height: return 0

        fr, to, res = 0, len(height)-1, 0
        while fr < to:
            res = max(res, min(height[fr], height[to])*(to-fr))
            if height[fr] < height[to]: fr += 1
            else: to -= 1

        return res

    ### 12. Integer to Roman ###
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        if not num: return ''

        int_roman = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
        i, res = 0, ''
        while i < len(int_roman):
            res += (num // int_roman[i][0]) * int_roman[i][1]
            num %= int_roman[i][0]
            i += 1

        return res

    ### 13. Roman to Integer ###
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        if not s: return 0

        i = j = res = 0
        int_roman = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
        while i < len(s):
            if s[i:].startswith(int_roman[j][1]):
                res += int_roman[j][0]
                i += len(int_roman[j][1])
            else: j += 1

        return res

    ### 14. Longest Common Prefix ###
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        strs = list(set(strs))
        strs.sort(key=lambda x: len(x), reverse=True)
        if not len(strs[-1]): return ''

        res = strs[0]
        for _ in xrange(1, len(strs)):
            l = min(len(res), len(strs[_]))
            for i in xrange(l):
                if res[i] != strs[_][i]:
                    l = i
                    break
            res = res[:l]
            if not res: break

        return res

    ### 15. 3Sum ###
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if not nums or len(nums) < 3: return []

        nums = sorted(nums)
        res = []
        for i in xrange(len(nums)):
            if i and nums[i] == nums[i-1]: continue
            fr, to, val = i+1, len(nums)-1, -nums[i]
            while fr < to:
                tmp = nums[fr] + nums[to]
                if tmp == val:
                    res.append([nums[i], nums[fr], nums[to]])
                if tmp <= val:
                    while fr < to and nums[fr] == nums[fr+1]: fr += 1
                    fr += 1
                if tmp >= val:
                    while fr < to and nums[to] == nums[to-1]: to -= 1
                    to -= 1

        return res

    ### 16. 3Sum Closest ###
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if not nums or len(nums) < 3: return sum(nums)

        nums = sorted(nums)
        diff = res = -1
        for i in xrange(len(nums)):
            if i and nums[i] == nums[i-1]: continue
            fr, to = i+1, len(nums)-1
            while fr < to:
                tmp = nums[i] + nums[fr] + nums[to]
                if diff == -1 or abs(tmp - target) < diff:
                    diff = abs(tmp - target)
                    res = tmp
                    if diff == 0: break
                if tmp < target:
                    while fr < to and nums[fr] == nums[fr+1]: fr += 1
                    fr += 1
                if tmp > target:
                    while fr < to and nums[to] == nums[to-1]: to -= 1
                    to -= 1
            if not diff: break

        return res

    ### 17. Letter Combinations of a Phone Number ###
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if not digits: return []

        digit_letters_mapper = {'0': ' ',
                                '1': '',
                                '2': 'abc',
                                '3': 'def',
                                '4': 'ghi',
                                '5': 'jkl',
                                '6': 'mno',
                                '7': 'pqrs',
                                '8': 'tuv',
                                '9': 'wxyz'}

        res = []
        def dfs(nums, path):
            if not nums:
                res.append(path)
                return
            for i in digit_letters_mapper[nums[0]]:
                dfs(nums[1:], path+i)

        dfs(digits, '')
        return res

    ### 18. 4Sum ###
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if not nums or len(nums) < 4: return []

        nums = sorted(nums)
        res = []
        for i in xrange(len(nums)-3):
            if i and nums[i] == nums[i-1]: continue
            if target-nums[i] < 3*nums[i+1] or target-nums[i] > 3*nums[-1]: continue
            for j in xrange(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                if target-nums[i]-nums[j] < 2*nums[j+1] or target-nums[i]-nums[j] > 2*nums[-1]: continue
                fr, to, val = j+1, len(nums)-1, target-nums[i]-nums[j]
                while fr < to:
                    tmp = nums[fr] + nums[to]
                    if tmp == val:
                        res.append([nums[i], nums[j], nums[fr], nums[to]])
                    if tmp <= val:
                        while fr < to and nums[fr] == nums[fr+1]: fr += 1
                        fr += 1
                    if tmp >= val:
                        while fr < to and nums[to] == nums[to-1]: to -= 1
                        to -= 1

        return res

    ### 19. Remove Nth Node From End of List ###
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if not head or not n: return head

        here = there = head
        while there and n >= 0:
            there = there.next
            n -= 1

        if not n:
            head = head.next
            here.next = None
            del here
            return head
        if not there and n >= 0: return head
        while there:
            here = here.next
            there = there.next
        there = here.next
        here.next = there.next
        there.next = None
        del there

        return head
