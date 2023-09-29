

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
       


    
    
    
        
