class Solution:
    ### 290. Word Pattern ###
    # @param {string} pattern
    # @param {string} str
    # @return {boolean}
    def wordPattern(self, pattern, str):
        can = str.split()
        if len(pattern) != len (can): return False

        flag, recl, recr = True, {}, {}
        for i in range(len(pattern)):
            if not recl.get(pattern[i]) and not recr.get(can[i]):
                recl[pattern[i]] = can[i]
                recr[can[i]] = pattern[i]
            elif recl.get(pattern[i]) != can[i] or recr.get(can[i]) != pattern[i]:
                flag = False
                break

        return flag

    ### 292. Nim Game ###
    # @param {integer} n
    # @return {boolean}
    def canWinNim(self, n):
        return n%4>0

    ### 299. Bulls and Cows ###
    # @param {string} secret
    # @param {string} guess
    # @return {string}
    def getHint(self, secret, guess):
        if not secret: '0A0B'

        cnt, bull, cow = [0]*10, 0, 0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bull += 1
            else: cnt[int(secret[i])] += 1
        for i in range(len(guess)):
            if secret[i] != guess[i]:
                d = int(guess[i])
                if cnt[d] > 0:
                    cnt[d] -= 1
                    cow += 1

        return str(bull)+'A'+str(cow)+'B'

    ### 300. Longest Increasing Subsequence ###
    # @param {integer[]} nums
    # @return {integer}
    def lengthOfLIS(self, nums):
        if not nums: return 0

        lis, res = [nums[0]], 1
        for x in nums[1:]:
            if x > lis[-1]:
                lis.append(x)
                res += 1
            else:
                l, r = 0, len(lis)
                while l <= r:
                    mid = (l+r) >> 1
                    if lis[mid] >= x: r = mid-1
                    else: l = mid+1
                lis[l] = x

        return res

    ### 301. Remove Invalid Parentheses ###
    # @param {string} s
    # @return {string[]}
    def removeInvalidParentheses(self, s):
        if not s: return ['']
        start, end, left, right = 0, len(s)-1, '', ''
        while True:
            if start<end and s[start] != '(':
                if s[start] != ')': left += s[start]
                start += 1
            if start<end and s[end] != ')':
                if s[end] != '(': right = s[end]+right
                end -= 1
            if start>=end or (s[start] == '(' and s[end] == ')'): break
        if start == end and s[start] in '()': return [left+right]
        s = left+s[start:end+1]+right

        def isValid(s):
            if not s: return True
            cnt = 0
            for x in s:
                if x == '(': cnt += 1
                if x == ')':
                    if cnt == 0: return False
                    cnt -= 1
            return cnt == 0

        head, found, record, queue, res = 0, False, set(), [s], []
        while head < len(queue):
            cur = queue[head]
            head += 1
            if isValid(cur):
                res.append(cur)
                found = True
            if found: continue
            for i in range(len(cur)):
                if cur[i] not in '()': continue
                tmp = cur[:i]+cur[i+1:]
                if tmp not in record:
                    record.add(tmp)
                    queue.append(tmp)

        return res

    ### 306. Additive Number ###
    # @param {string} num
    # @return {boolean}
    def isAdditiveNumber(self, num):
        if not num or len(num)<3: return False

        def dfs(a, b, c):
            if a[0] == '0' and len(a) > 1: return False
            if b[0] == '0' and len(b) > 1: return False
            d = str(int(a)+int(b))
            if not c.startswith(d): return False
            if len(c) == len(d): return True
            return dfs(b, d, c[len(d):])

        for i in xrange(1, len(num)//3+1):
            for j in xrange(i, i+(len(num)-i)//2):
                if dfs(num[:i], num[i:j+1], num[j+1:]): return True

        return False

    ### 309. Best Time to Buy and Sell Stock with Cooldown ###
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices: return 0

        pre, pre2, pre3, cur, res = 0, 0, 0, 0, 0
        for i in xrange(1, len(prices)):
            diff = prices[i]-prices[i-1]
            cur = max(cur, pre3)+diff
            res = max(res, cur)
            if i>2: pre3 = pre2
            if i>1: pre2 = pre
            pre = res

        return res
