# 146
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.pos = self.cnt = 0
        self.record = {}
        self.queue = []

    def _update(self):
        while self.cnt > self.capacity:
            key = self.queue[self.pos]
            if self.record[key][0] > 1:
                self.record[key][0] -= 1
            else:
                del self.record[key]
                self.cnt -= 1
            self.pos += 1

    # @return an integer
    def get(self, key):
        if key in self.record:
            self.queue.append(key)
            self.record[key][0] += 1
            return self.record[key][1]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.record:
            self.queue.append(key)
            self.record[key][0] += 1
            self.record[key][1] = value
        else:
            self.queue.append(key)
            self.record[key] = [1, value]
            self.cnt += 1
        self._update()

# 208
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.chd = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for x in word:
            idx = ord(x)-97
            if not cur.chd[idx]: cur.chd[idx] = TrieNode()
            cur = cur.chd[idx]
        cur.end = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        cur = self.root
        for x in word:
            idx = ord(x)-97
            cur = cur.chd[idx]
            if not cur: return False

        return cur.end

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        cur = self.root
        for x in prefix:
            idx = ord(x)-97
            cur = cur.chd[idx]
            if not cur: return False

        return True
