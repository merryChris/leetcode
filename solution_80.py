class Solution:
    # 88
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @param {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        while m and n:
            nums1[m+n-1] = max(nums1[m-1], nums2[n-1])
            if nums1[m-1] > nums2[n-1]: m -= 1
            else: n -= 1
        if n: nums1[0:n] = nums2[0:n]
        print nums1
        return

    # 89
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        return [(i>>1)^i for i in xrange(2**n)]
