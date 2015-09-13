class Solution:
    ### 1. Two Sum ###
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        record = {}
        for _ in xrange(len(nums)):
            record[nums[_]] = _
        for _ in xrange(len(nums)):
            if record.has_key(target-nums[_]) and record[target-nums[_]] > _:
                i, j = _, record[target-nums[_]]
                break

        return [i+1,j+1]

    ### 2. Add Two Numbers ###
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        def cnt(l):
            cur, c = l, 0
            while cur:
                cur = cur.next
                c += 1
            return c

        c1, c2 = cnt(l1), cnt(l2)
        if c1 < c2: l1, l2 = l2, l1
        head = pre = l1
        jin = 0
        while l2:
            tmp = l1.val + l2.val + jin
            l1.val = tmp % 10
            jin = tmp / 10
            pre = l1
            l1 = l1.next
            l2 = l2.next
        while l1 and jin:
            tmp = l1.val + jin
            l1.val = tmp % 10
            jin = tmp / 10
            pre = l1
            l1 = l1.next
        if not l1 and jin:
            pre.next = ListNode(jin)

        return head

    ### 3. Longest Substring Without Repeating Characters ###
    # @param {string} s
    # @param {integer}
    def lengthOfLongestSubstring(self, s):
        if not s: return 0

        head = tail = res = 0
        rec = set()
        while True:
            while tail < len(s) and s[tail] not in rec:
                rec.add(s[tail])
                tail += 1
            res = max(res, tail-head)
            if tail == len(s): break
            while True:
                rec.remove(s[head])
                head += 1
                if s[head-1] == s[tail]:
                    break

        return res

    ### 4. Median of Two Sorted Arrays ###
    # @param {list[int]} nums1
    # @param {list[int]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if not l: return None

        def findKth(A, B, k):
            if len(A) < len(B): A, B = B, A
            if not B: return A[k]
            if k == 0: return min(A[0], B[0])
            if k == len(A) + len(B) - 1: return max(A[-1], B[-1])

            j = min(k//2, len(B)-1)
            i = k-j-1
            if A[i] < B[j]: return findKth(A[i+1:], B[:j+1], j)
            elif A[i] > B[j]: return findKth(A[:i+1], B[j+1:], i)
            return A[i]

        if l & 1: return findKth(nums1, nums2, l//2)
        return (findKth(nums1, nums2, l//2-1) + findKth(nums1, nums2, l//2)) * 0.5

    ### 5. Longest Palindromic Substring ###
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if not s: return ''

        ss = '\001'.join(['']+list(s)+[''])
        dp = [0] * len(ss)
        pivot = right = res = bj= -1
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
            if dp[i] > res:
                res = dp[i]
                bj = i

        return ''.join(ss[bj-res+1:bj+res].split('\001'))

    ### 6. ZigZag Conversion ###
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if not s or not numRows: return ''
        if numRows == 1 or numRows >= len(s): return s

        l, res = (numRows-1)*2, ''
        for _ in xrange(numRows):
            pre, cur, unit = None, _, l-_*2
            while cur < len(s):
                if pre != cur: res += s[cur]
                pre = cur
                cur += unit
                unit = l-unit

        return res

    ### 7. Reverse Integer ###
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if not x: return x

        INT_MIN = -2147483648
        INT_MAX = 2147483647
        sign = -1 if x < 0 else 1
        res = int(str(abs(x))[::-1])*sign

        return res if res >= INT_MIN and res <= INT_MAX else 0

    ### 8. String to Integer (atoi) ###
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        str = str.strip()
        if not str: return 0

        INT_MIN = -2147483648
        INT_MAX = 2147483647
        str = list(str[::-1])
        sign, res = 0, 0
        while str:
            tmp = str.pop()
            if tmp in ('-', '+'):
                if not sign: sign = (tmp == '-') and -1 or 1
                else: return 0
            elif not tmp.isdigit(): break
            else:
                res *= 10
                res += int(tmp)
        if sign: res *= sign

        if res < INT_MIN: return INT_MIN
        if res > INT_MAX: return INT_MAX
        return res

    ### 9. Palindrome Number ###
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0: return False
        if not x: return True
        return str(x) == str(x)[::-1]
