class Solution:
    ### 20. Valid Parentheses ###
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if not s: return True

        left = ''
        for _ in s:
            if left and left[-1]+_  in ('()', '[]', '{}'): left=left[:-1]
            elif _ in '([{': left += _
            else: return False

        return not left

    ### 21. Merge Two Sorted Lists ###
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    ### 22. Generate Parentheses ###
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 0: return []

        parentheses = []
        def dfs(left, right, cur):
            if not left:
                parentheses.append(cur+')'*right)
                return
            if right: dfs(left,right-1,cur+')')
            dfs(left-1, right+1, cur+'(')
            return

        dfs(n,0,'')
        return parentheses

    ### 23. Merge k Sorted Lists ###
    # @param @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if not lists: return None

        nodes = []
        for cur in lists:
            while cur:
                nodes.append(cur)
                cur = cur.next
        if not nodes: return None
        nodes.sort(key=lambda x: x.val)
        tail = None
        while nodes:
            head = nodes.pop()
            head.next = tail
            tail = head

        return head

    ### 24. Swap Nodes in Pairs ###
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head or not head.next: return head

        dummy, nxt = head.next, head.next.next
        dummy.next = head
        head.next = self.swapPairs(nxt)

        return dummy

    ### 25. Reverse Nodes in k-Group ###
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head or k == 0 or k == 1: return head
        cnt, tail = 1, head
        while cnt < k:
            if not tail.next: return head
            tail = tail.next
            cnt += 1

        cnt, dummy, tail = 1, None, head
        while cnt <= k:
            tmp = head.next
            head.next = dummy
            dummy = head
            head = tmp
            cnt += 1

        tail.next = self.reverseKGroup(head, k)
        return dummy


    ### 26. Remove Duplicates from Sorted Array ###
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums: return 0

        tail = 0
        for i in xrange(1,len(nums)):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]
        nums = nums[:tail+1]
        return tail+1

    ### 27. Remove Element ###
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if not nums: return 0

        l, r = 0, len(nums)-1
        while True:
            while l <= r and nums[l] != val: l += 1
            while l <= r and nums[r] == val: r -= 1
            if l > r: break
            nums[l], nums[r] = nums[r], nums[l]

        return r+1

    ### 28. Implement strStr() ###
    # @param {string} haystack
    # @param {string} needle
    # @return {inetger}
    def strStr(self, haystack, needle):
        return haystack.find(needle)

    ### 29. Divide Two Integers ###
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if divisor == 0 or (dividend == INT_MIN and divisor == -1): return INT_MAX
        if dividend == 0: return 0

        sign = 1 if (dividend > 0) is (divisor > 0) else -1
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        for i in xrange(31,-1,-1):
            if (dividend >> i) >= divisor:
                res |= 1 << i
                dividend -= divisor << i

        return res*sign
