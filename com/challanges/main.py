from math import  trunc
from random import randint
from typing import List, Optional

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



            
  


    
    
    
        
