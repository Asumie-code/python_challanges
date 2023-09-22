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