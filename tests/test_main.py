import com.challanges.main as challanges



def test_func(): 
    assert challanges.roman_to_int('LVIII') == 58
    assert challanges.roman_to_int('MCMXCIV') == 1994
    assert challanges.roman_to_int('III') == 3
    