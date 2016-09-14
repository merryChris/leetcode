class Solution:
    ### 342. Power of Four ###
    # @param {integer} num
    # @return {boolean}
    def isPowerOfFour(self, num):
        if not num or (num & (num-1)): return False

        while num:
            if num&1: return True
            num >>= 2
        return False

    ### 343. Integer Break ###
    # @param {integer} n
    # @return {integer}
    def integerBreak(self, n):
        if n == 2: return 1
        if n == 3: return 2
        if n == 4: return 4
        if n == 5: return 6
        if n == 6: return 9
        return 3*self.integerBreak(n-3)

    ### 344. Reverse String ###
    # @param {string} s
    # @return {string}
    def reverseString(self, s):
        return s[::-1]

    ### 345. Reverse Vowels of a String ###
    # @param {string} s
    # @return {string}
    def reverseVowels(self, s):
        if not s: return s
        s = list(s)
        l, r = 0, len(s)-1
        while l < r:
            while l < r and s[l] not in 'aAeEiIoOuU': l += 1
            while l < r and s[r] not in 'aAeEiIoOuU': r -= 1
            if l < r: s[l], s[r] = s[r], s[l]; l += 1; r-= 1

        return ''.join(s)

    ### 347. Top K Frequent Elements ###
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def topKFrequent(self, nums, k):
        if not k: return []

        rec = {}
        for x in nums:
            if x not in rec: rec[x] = 0
            rec[x] += 1
        import heapq
        kfreq = set(heapq.nlargest(k, rec.values()))

        return [key for key,val in rec.items() if val in kfreq]

    ### 349. Intersection of Two Arrays ###
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {integer[]}
    def intersection(self, nums1, nums2):
        if not nums1 or not nums2: return []
        return list(set(nums1).intersection(set(nums2)))

    ### 350. Intersection of Two Arrays II ###
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {integer[]}
    def intersect(self, nums1, nums2):
        if not nums1 or not nums2: return []

        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        rec, res = {}, []
        for x in nums1:
            if x not in rec: rec[x] = 0
            rec[x] += 1
        for x in nums2:
            if x in rec:
                rec[x] -= 1
                res.append(x)
                if rec[x] == 0: rec.pop(x)

        return res

    ### 354. Russian Doll Envelopes ###
    # @param {integer[][]} envelopes
    # @return {integer}
    def maxEnvelopes(self, envelopes):
        if not envelopes: return 0

        envelopes.sort(key=lambda e: (e[0], -e[1]))
        dp = []
        for _, h in envelopes:
            l, r = 0, len(dp)-1
            while l <= r:
                mid = (l+r)/2
                if dp[mid] < h: l=mid+1
                else: r=mid-1
            if l == len(dp): dp.append(h)
            else: dp[l] = h

        return len(dp)

    ### 357. Count Numbers with Unique Digits ###
    # @param {integer} n
    # @return {integer}
    def countNumbersWithUniqueDigits(self, n):
        res, cur = 1, 1
        for i in range(min(n,10)):
            if i == 0: cur *= 9
            elif i <= 9: cur *= 10-i
            res += cur

        return res

    ### 363. Max Sum of Rectangle No Larger Than K ###
    # @param {integer[][]}
    # @param {integer} k
    # @return {integer}
    def maxSumSubmatrix(self, matrix, k):
        if not matrix or not matrix[0]: return 0

        import bisect
        res = float('-inf')
        for i in range(0, len(matrix[0])):
            val = [0] * len(matrix)
            for j in range(i, len(matrix[0])):
                rec, cur = [0], 0
                for p in range(len(matrix)):
                    val[p] += matrix[p][j]
                    cur += val[p]
                    pos = bisect.bisect_left(rec, cur-k)
                    if pos <= p:
                        res = max(res, cur-rec[pos])
                        if res == k: return k
                    bisect.insort(rec, cur)

        return res
