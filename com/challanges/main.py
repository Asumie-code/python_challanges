from math import  trunc
from random import randint
from typing import List, Optional
from queue import Queue

def roman_to_int(s):
    roman_num = s
    sum = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if "IX" in roman_num:
        roman_num = roman_num.replace("IX", "")
        sum += 9
    if "IV" in roman_num:
        roman_num = roman_num.replace("IV", "")
        sum += 4
    if "XL" in roman_num:
        roman_num = roman_num.replace("XL", "")
        sum += 40
    if "XC" in roman_num:
        roman_num = roman_num.replace("XC", "")
        sum += 90
    if "CD" in roman_num:
        roman_num = roman_num.replace("CD", "")
        sum += 400
    if "CM" in roman_num:
        roman_num = roman_num.replace("CM", "")
        sum += 900

    for c in roman_num:
        sum += roman[c]

    return sum


def long_prefix(v):
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 




def remove_duplicates(nums: list[int]) -> int: 
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2): 
    lis = []

    current = list1
    while current != None: 
        lis.append(current.val)
        current = current.next
   
    current = list2
    while current != None: 
         lis.append(current.val)
         current = current.next
    
    lis.sort()
 
    current = result = ListNode()
    for i in lis: 
        current.next = ListNode(i)
        current = current.next

    return result.next
       

def removeElement(nums, val): 
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index


def iofo(haystack, needle):
      if needle not in haystack: return -1 
      return haystack.find(needle)


def searchInsert(nums, target): 
    for index in range(len(nums)): 
        if nums[index] >= target: 
            return index 
    return len(nums)
     
def lengthOfLastWord(s): 
     return len(s.split()[-1])



def plusOne(digits):
    #neat solution  
    # if digits[-1] != 9:
    # digits[-1] += 1
    # return digits
    # num = 0
    # for el in digits:
    #     num = num * 10 + el
    # return [int(i) for i in str(num + 1)]

    digits.reverse()
    number = 0
    for index , x in enumerate(digits): 
        number += x * 10**index 
    number += 1 
    plusOne = []
    while number > 0: 
        number, remd = divmod(number, 10)
        plusOne.append(remd)
    plusOne.reverse()
    return plusOne


def plusOne_in_place_version( digits):
    if digits == [0]: return [1]

    carry = 1
    i = len(digits)-1
    while carry:
        digits[i] = (carry + digits[i]) % 10
        if digits[i] == 0: carry = 1
        else: carry = 0
        i -= 1

        if i < 0:
            if carry: digits.insert(0, 1)
            break
    return digits



def addBinary(a, b): 
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    carry = 0 
    for i in range(max_len - 1, -1, -1): 
        r = carry 
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1 
    if carry != 0: 
        result = '1' + result
    
    return result




def mysqrt(x): 
        if x == 0: return 0
        precision = 20 # increase precision increase the time 
        y = randint(1,x)
        square = 0
        while precision > 0:
            square = 0.5*(y + (x / y) )
            y = square
            precision -= 1 

        return trunc(square)



def climbStairs( n: int) -> int:
       if n == 0 or n == 1:
           return 1
       return climbStairs(n-1) + climbStairs(n-2)  


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    s = set()

    current = head 
    while current != None: 
        s.add(current.val)
        current = current.next
    lis = list(s)
    lis.sort()
    current = result = ListNode() 
    for i in lis: 
        current.next = ListNode(i)
        current = current.next 

    return result.next



def merge(nums1, m, nums2, n): 
    for i in range(n): 
        nums1[m + i] = nums2[i]
    nums1.sort()



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    current = root 
    stack = []
    result = []

    while True: 
        if current is not None: 
            stack.append(current)
            current = current.left 
        elif stack: 
            current = stack.pop()
            result.append(current.val)
            current = current.right
        else: 
            return result




def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None: 
        return True 
    if p is None or q is None: 
        return False 
    if p.val == q.val: 
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    return False


def isSymmetric(root: Optional[TreeNode]) -> bool:
    if root is None: return True
    def isSameTree(p, q):     
        if p is None and q is None: 
            return True 
        if p is None or q is None: 
            return False 
        if p.val == q.val: 
            return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)

        return False
    return isSameTree(root.left, root.right)

def maxDepth(root: Optional[TreeNode]) -> int:
    if root == None: return 0
    rightDepth = maxDepth(root.right)
    leftDepth = maxDepth(root.left)
    return 1 +  max(rightDepth, leftDepth)


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    total_nums = len(nums)
    if not total_nums: return None

    mid_node = total_nums // 2 

    return TreeNode(
        nums[mid_node], 
        sortedArrayToBST(nums[:mid_node]), 
        sortedArrayToBST(nums[mid_node + 1 :])
        )



def Height(root): 
    if root is None: return 0 
    leftheight, rightheight = Height(root.left), Height(root.right)
    if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1: 
        return -1
    return max(leftheight, rightheight) + 1
            
def isBalanced(root: Optional[TreeNode]) -> bool: 
    return Height(root) >= 0

def minDepth(root: Optional[TreeNode]) -> int: 
    if root is None: return 0 
    if root.left is None: return minDepth(root.right) + 1 
    if root.right is None : return minDepth(root.left) + 1 
    return min(minDepth(root.left), minDepth(root.right)) + 1
    
    
def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
      if root is None: return False
      ans = 0 
      subSum =  targetSum - root.val 


      if subSum == 0 and root.left == None and root.right == None: return True

      if root.left is not None: 
          ans = ans or hasPathSum(root.left, subSum)  

      if root.right is not None: 
          ans = ans or hasPathSum(root.right, subSum)  
      return ans

#pascal's triangle 1
def generate(numRows: int) -> List[List[int]]: 
    if numRows == 0: 
        return []
    if numRows == 1: 
        return [[1]]
    
    prevRows = generate(numRows - 1)
    newRow = [1] * numRows

    for i in range(1, numRows - 1): 
        newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
    
    prevRows.append(newRow)
    return prevRows



def getRow(rowIndex: int) -> List[int]: 
    res = [1]
    prev = 1 
    for k in range(1, rowIndex + 1): 
        next_val = prev * (rowIndex - k + 1) // k 
        res.append(next_val)
        prev = next_val 
    return res


def maxProfit(prices: List[int]) -> int:
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit


def singleNumber(nums: List[int]) -> int:
        for i in range(1, len(nums)): 
            nums[i] = nums[i] ^ nums[i - 1]

        return nums[-1]




def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False

    return True



def hasCycle(head: Optional[ListNode]) -> bool: 
    fast = head 
    while fast and fast.next: 
        head = head.next
        fast = fast.next.next
        if head is fast: 
            return True
    return False



def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if root == None: return 
    st = []
    data = [] 
    current = root 

    while len(st) or current != None: 
        while(current != None): 
            data.append(current.val)

            if current.right != None: 
                st.append(current.right)
            current = current.left
        if len(st) > 0: 
            current = st[-1]
            st.pop()
    
    return data


def postorderTraversal( root: Optional[TreeNode]) -> List[int]:
        stack = []
        data = []
        while True: 
            while(root != None): 
                stack.append(root)
                stack.append(root)
                root = root.left 

            if len(stack) == 0: return data 

            root = stack.pop() 

            if len(stack) > 0 and stack[-1] == root: 
                root = root.right
            else: 
                data.append(root.val)
                root = None




def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0 
        nodeA, nodeB = headA, headB 
        while nodeA: 
            lenA += 1 
            nodeA = nodeA.next
        while nodeB: 
            lenB += 1 
            nodeB = nodeB.next

        diff = abs(lenA - lenB)
        if lenA > lenB: 
            while diff > 0: 
                headA = headA.next 
                diff -= 1 
        else: 
            while diff > 0: 
                headB = headB.next
                diff -= 1 

        while headA and headB: 
            if headA == headB: 
                return headA
            headA = headA.next 
            headB = headB.next
        return None
## linked list intersection 


def convertToTitle(columnNumber: int) -> str: 
    if not columnNumber: 
        return ''
    columnNumber , remainder = divmod(columnNumber - 1, 26 )
    return convertToTitle(columnNumber) + chr(65 + remainder)


def majorityElement(nums: List[int]) -> int: 
    count = 0 
    majority = 0 
    for num in nums: 
        if count == 0: 
            majority = num 
        if num == majority: 
            count += 1 
        else: 
            count -= 1
    return majority

def titleToNumber(columnTitle: str) -> int: 
    col_num = 0
    for char in columnTitle: 
        col_num = col_num * 26 +(ord(char) - 64)
    return col_num


def reverseBits(n: int) -> int: 
        result = 0
        for _ in range(32):
            result |= n&1
            result <<= 1
            n >>= 1

        result >>= 1
        return result


def hammingWeight(n: int) -> int: 
    count  = 0 
    while n: 
        n &= n -1 
        count += 1 
    return count 


def pdi_function(number, base: int = 10): 
    total = 0 
    while number > 0: 
        total += pow(number % base, 2)
        number = number // base 
    return total

def isHappy(number: int) -> bool: 
    seen_numbers = set() 
    while number > 1 and number not in seen_numbers: 
        seen_numbers.add(number)
        number = pdi_function(number)
    return number == 1

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]: 
    dummy = ListNode(next=head)
    prev, curr = dummy, head 
    while curr: 
        if curr.val == val: 
            nxt = curr.next 
            prev.next = nxt 
            curr = nxt
        else: 
            prev = curr 
            curr = curr.next
    return dummy.next


def isIsomorphic(s: str, t: str) -> bool: 
    if len(s) != len(t): return False
    map1 = []
    map2 = []
    for idx in s: 
        map1.append(s.index(idx))
    for idx in t: 
        map2.append(t.index(idx))
    if map1 == map2: 
        return True 
    return False


def reverseList( head: Optional[ListNode]) -> Optional[ListNode]:
    new_list = None 
    current = head 

    while current: 
        next_node = current.next 
        current.next = new_list 
        new_list = current 
        current = next_node 
    return new_list





def containsDuplicate(nums: List[int]) -> bool: 
    no_repeats = len(set(nums))
    return no_repeats < len(nums)

def containsNearbyDuplicate(nums: List[int], k: int) -> bool: 
    d = {}

    for i, n in enumerate(nums): 
        if n in d and abs(i - d[n]) <= k: 
            return True
        else: 
            d[n] = i
    return False


def countNodes(root: Optional[TreeNode]) -> int: 
    count = 0
    current = root 

    while current: 
        if current.left is None: 
            count += 1 
            current = current.right
        else: 
            prev = current.left
            while prev.right and prev.right != current:
                prev = prev.right

            if prev.right is None: 
                prev.right = current 
                current = current.left 
            else: 
                prev.right = None
                count += 1 
                current = current.right 
    return count




class MyStack:
    def __init__(self):
        self.q = Queue()
        self.topp = -1

    def push(self, x):
        self.q.put(x)
        self.topp = x
        size = self.q.qsize()
        while size > 1:
            front = self.q.get()
            self.q.put(front)
            size -= 1

    def pop(self):
        remo = self.q.get()
        if not self.q.empty():
            self.topp = self.q.queue[0]
        return remo

    def top(self):
        return self.topp

    def empty(self):
        return self.q.empty()

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:

    if root == None: return
    else: 
        temp = root 

        invertTree(root.left)
        invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp
    return root


def summaryRanges(nums: List[int]) -> List[str]: 
    ans = []

    i = 0 
    while i < len(nums):
        begin = nums[i]
        while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1: 
            i += 1
        end = nums[i]
        if begin == end: 
            ans.append(str(begin))
        else: 
            ans.append(str(begin) + '->' + str(end))
        i += 1

    return ans
         

def isPowerOfTwo(n: int) -> bool: 
    return (n and (not(n & (n - 1))))


class MyQueue: 
    def __init__(self): 
        self.s1 = []
        self.s2 = []

    def push(self, x) -> None: 
        while self.s2: 
            self.s1.append(self.s2.pop())
        self.s1.append(x)
        while self.s1: 
            self.s2.append(self.s1.pop())
    
    def pop(self) -> int: 
        return self.s2.pop()

    def peek(self) -> int: 
        return self.s2[-1]
    def empty(self) -> bool: 
        return not bool(self.s2)
    


def isPalindrome_Lis(head: Optional[ListNode]) -> bool:
    slow, fast, prev = head, head, None
    while fast and fast.next: 
        slow, fast = slow.next, fast.next.next
    prev, slow, prev.next = slow, slow.next, None
    while slow: 
        slow.next, prev, slow = prev, slow, slow.next 
    fast, slow = head, prev 
    while slow: 
        if fast.val != slow.val: return False
        fast, slow = fast.next, slow.next
    return True


def isAnagram(s: str, t: str) -> bool:
    lisS = list(s)
    lisT = list(t)
    lisS.sort()
    lisT.sort() 
    return lisS == lisT