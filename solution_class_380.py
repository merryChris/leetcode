### 380. Insert Delete GetRandom O(1) ###
class RandomizedSet(object):

    # Initialize your data structure here.
    def __init__(self):
      self.nums, self.hsh = [], {}

    # Inserts a value to the set. Returns true if the set did not already contain the specified element.
    # @param {integer} val
    # @return {boolean}
    def insert(self, val):
      if val in self.hsh: return False

      self.hsh[val] = len(self.nums)
      self.nums.append(val)
      return True

    # Removes a value from the set. Returns true if the set contained the specified element.
    # @param {integer} val
    # @return {boolean}
    def remove(self, val):
      if val not in self.hsh: return False

      self.hsh[self.nums[-1]] = self.hsh[val]
      self.nums[self.hsh[val]] = self.nums[-1]
      self.nums.pop()
      self.hsh.pop(val)
      return True

    # Get a random element from the set.
    # @return {integer}
    def getRandom(self):
      import random
      return random.choice(self.nums)

### 381. Insert Delete GetRandom O(1) - Duplicates allowed ###
class RandomizedCollection(object):
    # Initialize your data structure here.
    def __init__(self):
      self.nums, self.hsh = [], {}

    # Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
    # @param {integer} val
    # @return {boolean}
    def insert(self, val):
      if val not in self.hsh: self.hsh[val] = set()

      self.hsh[val].add(len(self.nums))
      self.nums.append(val)
      return len(self.hsh[val]) == 1

    # Removes a value from the collection. Returns true if the collection contained the specified element.
    # @param {integer} val
    # @return {boolean}
    def remove(self, val):
      if val not in self.hsh: return False

      pos = self.hsh[val].pop()
      if pos != len(self.nums)-1:
        self.hsh[self.nums[-1]].remove(len(self.nums)-1)
        self.hsh[self.nums[-1]].add(pos)
      self.nums[pos] = self.nums[-1]
      if not self.hsh[val]: self.hsh.pop(val)
      self.nums.pop()
      return True

    # Get a random element from the collection.
    # @return {integer}
    def getRandom(self):
      import random
      return random.choice(self.nums)

### 382. Linked List Random Node ###
class RandomNodes(object):

  # @param {ListNode} head The linked list's head.
  # Note that the head is guaranteed to be not null, so it contains at least one node.
  def __init__(self, head):
    self.head = head

  # @return {integer} Returns a random node's value.
  def getRandom(self):
    res, l, cur = 0, 0, self.head

    import random
    while cur:
      l += 1
      if int(random.random() * l) == 0:
        res = cur.val
      cur = cur.next
    return res

### 384. Shuffle an Array ###
class Solution(object):

  # @param {integer[]} nums
  def __init__(self, nums):
    self.nums = nums

  # @return {integer[]}
  # Resets the array to its original configuration and return it.
  def reset(self):
    return self.nums

  # @return {integer[]}
  # Returns a random shuffling of the array.
  def shuffle(self):
    res = [_ for _ in self.nums]
    import random
    random.shuffle(res)
    return res

### 398. Random Pick Index ###
class Solution(object):

  # @param {integer[]}
  def __init__(self, nums):
    self.nums = nums

  # @param {integer} target
  # @return {integer}
  def pick(self, target):
    import random
    idx, cnt = -1, 0
    for i, num in enumerate(self.nums):
      if num == target:
        if random.randint(0, cnt) == 0: idx = i
        cnt += 1

    return idx
