class Node: 
    def __init__(self, val): 
        self.value = val
        self.next = None
        self.prev = None

class LinkedList: 
    def __init__(self, *values):
        self._length = 0
        self._head = self._tail = None
    
    @property
    def head(self): 
        return self._head
    
    @property
    def tail(self): 
        return self._tail
    
    @property
    def length(self):
        return self._length
    
    def append(self, val, checkDuplicates): 
        if checkDuplicates and self._isDuplicate(val): 
            return False

        newItem = Node(val)
        if not self._tail: 
            self._head = self._tail = newItem
        else: 
            self._tail.next = newItem
            newItem.prev = self._tail
            self._tail = newItem
        self._length += 1
        return True


    def toList(): 
        pass

    def _isDuplicate(self, val): 
        s = set(self.toList())
        return val in s
        