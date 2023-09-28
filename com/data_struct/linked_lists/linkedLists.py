class Node: 
    def __init__(self, val): 
        self.value = val
        self.next = None
        self.prev = None

class LinkedList: 
    def __init__(self, *values):
        self._length = 0
        self._head = self._tail = None
        
        if len(values) > 0: 
            for i in values: 
                self.append(i)
    
    def __iter__(self): 
        currentItem = self._head

        while currentItem: 
            yield currentItem.value
            currentItem = currentItem.next



    @property
    def head(self): 
        return self._head
    
    @property
    def tail(self): 
        return self._tail
    
    @property
    def length(self):
        return self._length
    
    def append(self, val, checkDuplicates = False): 
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

    
    def prepand(self, val, checkDuplicates = False): 
        if checkDuplicates and self._isDuplicate(val): 
            return False
        
        newItem = Node(val)

        if self._head: 
            self._head = self._tail = newItem
        else: 
            newItem.next = self._head
            self._head.prev = newItem
            self._head = newItem

        self._length += 1
        return True
    
    def insert(self, val, previousItem, checkDuplicates = False): 
        if checkDuplicates and self._isDuplicate(val): 
            return False
        newItem = Node(val)
        currentItem = self._head

        if not currentItem: 
            return False
        else: 
            while True: 
                if currentItem.value == previousItem: 
                    newItem.next = currentItem.next 
                    newItem.prev = currentItem
                    currentItem.next = newItem

                    if newItem.next: 
                        newItem.next.prev = newItem
                    else: 
                        self._tail = newItem

                    self._length += 1
                    return True
                else: 
                    if currentItem.next: 
                        currentItem = currentItem.next
                    else: 
                        return False
            
    def remove(self, val): 
        currentItem = self._head

        if not currentItem: return

        if currentItem.value == val: 
            self._head = currentItem.next
            self._head.prev = None
            currentItem.next = currentItem.prev = None
            self._length -=1 
            return currentItem.value
        else: 
            while True: 
                if currentItem.value == val: 
                    if currentItem.next:
                        currentItem.prev.next = currentItem.next
                        currentItem.next.prev = currentItem.prev
                        currentItem.next = currentItem.prev = None
                    else: 
                        currentItem.prev.next = None
                        self._tail = currentItem.prev
                        currentItem.next = currentItem.prev = None
                    
                    self._length -= 1
                    return currentItem.value
                else: 
                    if currentItem.next: currentItem = currentItem.next
                    else: return


    def removeHead(self): 
        currentItem = self._head

        if not currentItem: return 

        if not self._head.next: 
            self._head = None 
            self._tail = None
        else: 
            self._head.next.prev = None 
            self._head = self._head.next 
            currentItem.next = currentItem.prev = None
        
        self._length -= 1
        return currentItem.value
    

    def removeTail(self):
        currentItem = self._tail

        if not currentItem: return

        if not self._tail.prev: 
            self._head = None 
            self._tail = None
        else: 
            self._tail.prev.next = None 
            self._tail = self._tail.prev 
            currentItem.next = currentItem.prev = None
        
        self._length -= 1 
        return currentItem.value

    def toList(self): 
        return [*self]

    def _isDuplicate(self, val): 
        s = set(self.toList())
        return val in s
        

lis = LinkedList(1,2,4,5,6)
print(lis.toList())
for i in lis: 
    print(i)