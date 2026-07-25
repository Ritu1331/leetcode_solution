class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.mp = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.mp:
            return False

        self.arr.append(val)
        self.mp[val] = len(self.arr)-1

        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.mp:
            return False

        index = self.mp[val]

        last = self.arr[-1]

        self.arr[index] = last

        self.mp[last] = index

        self.arr.pop()

        del self.mp[val]

        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()