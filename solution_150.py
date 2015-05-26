class Solution:
    ### 150. Evaluate Reverse Polish Notation ###
    # @param {string{}} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(i)
            else:
                sec = stack.pop()
                fir = stack.pop()
                if i == '/':
                    fir = int(fir)
                    sec = int(sec)
                    ans = fir/sec + (fir*sec < 0 and fir%sec and 1 or 0)
                else:
                    ans = eval(fir+i+sec)
                stack.append(str(ans))

        return int(stack.pop())

    ### 151. Reverse Words in a String ###
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])

    ### 152. Maximum Product Subarray ###
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        ans = A[0]
        B = []
        C = []
        for i in xrange(len(A)):
            if i == 0:
                B.append(A[0])
                C.append(A[0])
            else:
                b = max(B[-1]*A[i], A[i], C[-1]*A[i])
                c = min(C[-1]*A[i], A[i], B[-1]*A[i])
                B.append(b)
                C.append(c)
                ans = max(ans, b)

        return ans

    ### 153 & 154. Find Minimum in Rotated Sorted Array ###
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l = 0
        r = len(num)-1
        if r<0: return None
        if r>=0 and num[l] < num[r]: return num[l]

        while l<r-1:
            mid = (l+r)>>1
            if num[mid] > num[l]: l=mid
            elif num[mid] < num[r]: r=mid
            else: return min(self.findMin(num[l:mid]), self.findMin(num[mid:r+1]))

        return min(num[l], num[r])

    ### 160. Intersection of Two Linked Lists ###
    # @param two ListNodes
    # return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        flag = None
        cnt = 0
        ha = headA
        hb = headB

        while ha and hb and cnt < 3:
            if ha == hb:
                flag = ha
                break
            ha = ha.next
            hb = hb.next
            if ha == None:
                cnt += 1
                ha = headB
            if hb == None:
                cnt += 1
                hb = headA

        return flag

    ### 162. Find Peak Element ###
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        n = len(num)
        if n <= 1: return 0

        l = 0
        r = n-1
        while l<r-2:
            mid = (l+r)>>1
            mmid = (mid+r)>>1
            if num[mid] < num[mmid]: l=mid
            else: r=mmid

        if (l == 0 or num[l] > num[l-1]) and num[l] > num[l+1]: return l
        if num[l+1] > num[l] and (l+2 == n or num[l+1] > num[l+2]): return l+1
        return l+2

    ### 164. Maximum Gap ###
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        n = len(num)
        if n < 2: return 0

        min_num = min(num)
        max_num = max(num)
        step = max(1, (max_num-min_num)/n)
        bucket = [[(1<<32)+1, -1] for i in xrange(min_num, max_num+1, step)]

        for i in num:
            idx = (i - min_num) / step
            bucket[idx][0] = min(bucket[idx][0], i)
            bucket[idx][1] = max(bucket[idx][1], i)

        ans = 0
        pre = -1
        for i in bucket:
            if pre != -1 and i[0] != (1<<32)+1:
                ans = max(ans, i[0] - pre)
            if i[1] != -1:
                pre = i[1]

        return ans

    ### 165. Compare Version Numbers ###
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        category1 = map(int, version1.split('.'))
        category2 = map(int, version2.split('.'))
        while len(category1) and category1[-1] == 0: category1.pop()
        while len(category2) and category2[-1] == 0: category2.pop()

        ans = 0
        len1 = len(category1)
        len2 = len(category2)
        for i in xrange(min(len1, len2)):
            ans = (category1[i] > category2[i] or 0) and 1
            if ans: break;
            ans = (category1[i] < category2[i] or 0) and -1
            if ans: break;

        if ans == 0: ans = (len1 > len2 and 1) or (len1 < len2 and -1) or 0

        return ans

    ### 166. Fraction to Recurring Decimal ###
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        flag = None
        if numerator * denominator < 0: flag = True
        numerator = abs(numerator)
        denominator = abs(denominator)
        integer_part = (flag and '-' or "" ) + str(numerator / denominator)
        decimal_part = ""

        record = set()
        position = []
        remainder = numerator - numerator / denominator * denominator
        if remainder == 0: return integer_part

        while remainder:
            remainder *= 10
            mark = remainder / denominator
            remainder %= denominator
            if (mark, remainder) in record: break
            else: record.add((mark, remainder)); decimal_part += str(mark); position.append((mark, remainder))

        if remainder:
            pos = position.index((mark, remainder))
            decimal_part = decimal_part[:pos] + '(' + decimal_part[pos:] + ')'

        return integer_part + '.' + decimal_part


    ### 168. Excel Sheet Column Title ###
    # @return a string
    def convertToTitle(self, num):
        cnt = []
        while num:
            cnt.append(num%26)
            num /= 26

        ans = ""
        l = len(cnt)
        for i in xrange(l):
            if cnt[i] == 0:
                if i < l-1:
                    ans += 'Z'
                    cnt[i+1] -= 1
            else: ans += chr(65 + cnt[i] - 1)

        return ans[::-1]

    ### 169. Majority Element ###
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        half = len(num)/2
        cnt = []
        for x in xrange(32): cnt.append(0)
        for i in num:
            j = 0
            while i and j < 32:
                if i & 1: cnt[j] += 1
                j += 1
                i >>= 1

        ans = 0
        for i in xrange(32):
            if cnt[i] > half:
                ans |= 1 << i

        if (ans >= 2147483648): ans -= 4294967296

        return ans

    ### 171. Excel Sheet Column Number ###
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        ans = 0
        for i in xrange(len(s)):
            ans *= 26
            ans += ord(s[i]) - 64

        return ans

    ### 172. Factorial Trailing Zeroes ###
    # @return an integer
    def trailingZeroes(self, n):
        ans = 0
        while n:
            ans += n / 5
            n /= 5

        return ans

    ### 174. Dungeon Game ###
    # @param dungeon, a list of lists of integers
    # @return an integer
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        for i in xrange(0, m+n-1):
            for j in xrange(max(0,i-n+1), min(m,i+1)):
                x = m-1-j
                y = n-1-i+j
                ans = None
                if x != m-1: ans = dungeon[x+1][y]-dungeon[x][y]
                if y != n-1: ans = ans and min(ans, dungeon[x][y+1]-dungeon[x][y]) or dungeon[x][y+1]-dungeon[x][y]
                if ans == None: ans = max(1, 1-dungeon[x][y])
                dungeon[x][y] = max(1, ans)

        return dungeon[0][0]

    ### 179. Largest Number ###
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        return str(int("".join(sorted(map(str, num), key=lambda x: float(x)/(10**len(x)-1), reverse=True))))
        #return str(int("".join(sorted(map(str, num), cmp=lambda x, y: cmp(int(x+y), int(y+x)), reverse=True))))
