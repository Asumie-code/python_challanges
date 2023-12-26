from typing import List, Optional
import com.challanges.main as challanges



def test_roman_to_int(): 
    assert challanges.roman_to_int('LVIII') == 58
    assert challanges.roman_to_int('MCMXCIV') == 1994
    assert challanges.roman_to_int('III') == 3
    

def test_long_prefix(): 
    assert challanges.long_prefix(["flower","flow","flight"]) =="fl"
    assert challanges.long_prefix(["dog","racecar","car"]) ==""



def test_remove_duplicates(): 
    assert challanges.remove_duplicates([1,1,2,2,3,3])  == 3
    assert challanges.remove_duplicates([1,1,2,2,3,3,5,5])  == 4


def test_mergeTwoLists(): 
    lis1 = [1,2,4]
    lis2 = [1,3,5]
    result = lis1 + lis2
    result.sort()
    current = dummylis1 = challanges.ListNode()
    for i in lis1: 
        current.next = challanges.ListNode(i)
        current = current.next
    lis_node_1 = dummylis1.next


    current = dummylis2 = challanges.ListNode()
    for i in lis2: 
        current.next = challanges.ListNode(i)
        current = current.next
    lis_node_2 = dummylis2.next


    lis_node_result = challanges.mergeTwoLists(lis_node_1, lis_node_2) 
    current = lis_node_result 
    for i in result: 
        if current:
            assert current.val == i 
            current = current.next




def test_removeElement(): 
    assert challanges.removeElement([3,2,2,3], 3) == 2
    assert challanges.removeElement([0,1,2,2,3,0,4,2], 2) == 5



def test_iofo(): 
    assert challanges.iofo('sadbutsad', 'sad') == 0 
    assert challanges.iofo('sadbutsad', 'sado') == -1 


def test_searchInsert(): 
    assert challanges.searchInsert([1,3,5,6], 5) == 2
    assert challanges.searchInsert([1,3,5,6], 2) == 1


def test_lengthOfLastWord(): 
    assert challanges.lengthOfLastWord("hello world") == 5 
    assert challanges.lengthOfLastWord("  fly me  to  the moon   ") == 4


def test_plusOne(): 
    assert challanges.plusOne([1,2,3]) == [1,2,4]
    assert challanges.plusOne([9]) == [1,0]


def test_addBinary(): 
    assert challanges.addBinary('11', '1') == '100'
    assert challanges.addBinary('1010', '1011') == '10101'


def test_mysqrt(): 
    assert challanges.mysqrt(4) == 2
    assert challanges.mysqrt(8) == 2 
    assert challanges.mysqrt(0) == 0 
    assert challanges.mysqrt(9) == 3 



def test_climbStairs(): 
    assert challanges.climbStairs(3) == 3
    assert challanges.climbStairs(4) == 5


def test_deleteDuplicates(): 
   lis1 = [1,1,2]

   current = dummylis1 = challanges.ListNode()
   for i in lis1: 
        current.next = challanges.ListNode(i)
        current = current.next
   lis_node_1 = dummylis1.next

   result = challanges.deleteDuplicates(lis_node_1)

   current = result
   s  = set(lis1)
   for i in s: 
       if current: 
           assert i == current.val
           current = current.next
       

def test_inorderTraversal(): 
    root = challanges.TreeNode(1)
    root.left = challanges.TreeNode(2)
    root.right = challanges.TreeNode(3)
    root.left.left = challanges.TreeNode(4)
    root.left.right = challanges.TreeNode(5)

    assert challanges.inorderTraversal(root) == [4,2,5,1,3]



def test_isSameTree(): 
    root = challanges.TreeNode(1)
    root.left = challanges.TreeNode(2)
    root.right = challanges.TreeNode(3)
    root.left.left = challanges.TreeNode(4)
    root.left.right = challanges.TreeNode(5)
    root2  = challanges.TreeNode(1)
    root2.right = challanges.TreeNode(2)

    root3 = challanges.TreeNode(1)
    root3.left = challanges.TreeNode(2)

    assert challanges.isSameTree(root , root) == True 
    assert challanges.isSameTree(root2, root3) == False




def test_isSymmetric(): 
    root = challanges.TreeNode(1)
    root.left = challanges.TreeNode(2)
    root.right = challanges.TreeNode(3)
    root.left.left = challanges.TreeNode(4)
    root.left.right = challanges.TreeNode(5)

    root2 = challanges.TreeNode(1)
    root2.left = challanges.TreeNode(2)
    root2.right = challanges.TreeNode(2)



    assert challanges.isSymmetric(root ) == False 
    assert challanges.isSymmetric(root2) == True


def test_maxDepth(): 
    root = challanges.TreeNode(1)
    root.left = challanges.TreeNode(2)
    root.right = challanges.TreeNode(3)
    root.left.left = challanges.TreeNode(4)
    root.left.right = challanges.TreeNode(5)

    root2 = challanges.TreeNode(1)
    root2.left = challanges.TreeNode(2)
    root2.right = challanges.TreeNode(2)



    assert challanges.maxDepth(root ) ==  3
    assert challanges.maxDepth(root2) == 2


def test_sortedArrayToBST(): 
    nums  = [1,2,3,4,5]
    root = challanges.sortedArrayToBST(nums)
    assert type(root) == challanges.TreeNode
    rootValues = challanges.inorderTraversal(root)

    for i in rootValues: 
        assert i in nums


def test_isBalanced(): 
    root = challanges.TreeNode(1)
    root.left = challanges.TreeNode(2)
    root.right = challanges.TreeNode(3)
    root.left.left = challanges.TreeNode(4)
    root.left.right = challanges.TreeNode(5)

    assert challanges.isBalanced(root) == True

def test_minDepthg(): 
    root = challanges.TreeNode(1)
    root.left = challanges.TreeNode(2)
    root.right = challanges.TreeNode(3)
    root.left.left = challanges.TreeNode(4)
    root.left.right = challanges.TreeNode(5)

    assert challanges.minDepth(root) == 2 



def test_hasPathSum(): 
    root = challanges.TreeNode(1)
    root.left = challanges.TreeNode(2)
    root.right = challanges.TreeNode(3)
    root.left.left = challanges.TreeNode(4)
    root.left.right = challanges.TreeNode(5)

    assert challanges.hasPathSum(root, 7) == True  



def test_generate(): 
    assert challanges.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


def test_getRows(): 
    assert challanges.getRow(3) == [1,3,3,1]


def test_maxProfit(): 
    assert challanges.maxProfit([7,1,5,3,6,4]) == 5
    


def test_singleNumber(): 
    assert challanges.singleNumber([4,1,2,1,2]) == 4

def test_isPalindrome(): 
    assert challanges.isPalindrome("A man, a plan, a canal: Panama") == True

def test_hasCycle(): 
    lis1 = [3,2,0,-4]
    current = dummylis1 = challanges.ListNode()
    for i in lis1: 
        current.next = challanges.ListNode(i)
        current = current.next
        if i == lis1[-1]:
            current.next = dummylis1.next
    lis_node_1 = dummylis1.next
    assert challanges.hasCycle(lis_node_1) == True

def test_preorderTraversal(): 
    root = challanges.TreeNode(1)
    root.left = challanges.TreeNode(2)
    root.right = challanges.TreeNode(3)
    root.left.left = challanges.TreeNode(4)
    root.left.right = challanges.TreeNode(5)

    assert challanges.preorderTraversal(root) == [1,2,4,5,3]



def test_postorderTraversal(): 
    root = challanges.TreeNode(1)
    root.left = challanges.TreeNode(2)
    root.right = challanges.TreeNode(3)
    root.left.left = challanges.TreeNode(4)
    root.left.right = challanges.TreeNode(5)

    assert challanges.postorderTraversal(root) == [4,5,2,3,1]


def test_getIntersectionNode(): 
    common = challanges.ListNode(15)

    headA = challanges.ListNode(3)
    headA.next = challanges.ListNode(6)
    headA.next.next = challanges.ListNode(9)
    headA.next.next.next = common
    headA.next.next.next.next = challanges.ListNode(30)

    headB = challanges.ListNode(10)
    headB.next = common
    headB.next.next = challanges.ListNode(30)

    assert challanges.getIntersectionNode(headA, headB) == common

def test_convertToTitle(): 
    assert challanges.convertToTitle(28) == 'AB'
    assert challanges.convertToTitle(1) == 'A'

def test_majorityElement(): 
    assert challanges.majorityElement([1,1,1,1,2,4,5,5]) == 1

def test_titleToNumber(): 
    assert challanges.titleToNumber('A') == 1
    assert challanges.titleToNumber('AB') == 28
    assert challanges.titleToNumber('ZY') == 701