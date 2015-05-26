class Solution:
    ### 82. Remove Duplicates from Sorted List II ###
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head: return head

        dummy = ListNode(None)
        cur = head
        head = dummy
        while cur:
            dup = False
            while cur.next and cur.val == cur.next.val:
                dup = True
                cur = cur.next
            if not dup:
                dummy.next = cur
                dummy = dummy.next
            cur = cur.next

        dummy.next = None
        return head.next

    ### 83. Remove Duplicates from Sorted List ###
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicatesI(self, head):
        if not head or not head.next: return head

        pre, cur = head, head.next
        while cur:
            if pre.val < cur.val:
                pre.next = cur
                pre = pre.next
            cur = cur.next
        pre.next = cur

        return head

    ### 84. Largest Rectangle in Histogram ###
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        if not height: return 0

        l = len(height)
        area, stack = 0, [0]
        for i in xrange(1,l):
            while stack and height[stack[-1]] >= height[i]:
                h = height[stack.pop()]
                w = i if not stack else i-stack[-1]-1
                area = max(area, w*h)
            stack.append(i)
        while stack:
            h = height[stack.pop()]
            w = l if not stack else l-stack[-1]-1
            area = max(area, w*h)

        return area

    ### 85. Maximal Rectangle ###
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        if not matrix: return 0

        m, n = len(matrix), len(matrix[0])
        cnt = [int(x) for x in matrix[0]]
        area = 0
        for i in xrange(m):
            if i > 0:
                for j in xrange(n):
                     cnt[j] = 0 if matrix[i][j] == '0' else cnt[j]+1
            area = max(area, self.largestRectangleArea(cnt))

        return area

    ### 86. Partition List ###
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        d1 = ListNode(-1)
        d2 = ListNode(-1)
        cur = head
        head, tail = d1, d2
        while cur:
            if cur.val < x:
                d1.next = cur
                d1 = d1.next
            else:
                d2.next = cur
                d2 = d2.next
            cur = cur.next

        d1.next = tail.next
        d2.next = None
        return head.next

    ### 87. Scramble String ###
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    #def isScramble(self, s1, s2):

    ### 88. Merge Sorted Array ###
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

    ### 89. Gray Code ###
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        return [(i>>1)^i for i in xrange(2**n)]
