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