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
