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

        return [k for k,v in rec.items() if v in kfreq]

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
