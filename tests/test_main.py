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