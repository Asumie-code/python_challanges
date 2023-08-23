



def roman_to_int(s): 
    roman_num = s
    sum = 0
    roman = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000
    }
    
    if 'IX' in roman_num :
            roman_num = roman_num.replace('IX', '')
            sum += 9
    if 'IV' in roman_num :
            roman_num = roman_num.replace('IV', '')
            sum += 4 
    if 'XL' in roman_num :
            roman_num = roman_num.replace('XL', '')
            sum += 40 
    if 'XC' in roman_num :
            roman_num = roman_num.replace('XC', '')
            sum += 90
    if 'CD' in roman_num :
            roman_num = roman_num.replace('CD', '')
            sum += 400 
    if 'CM' in roman_num: 
            roman_num = roman_num.replace('CM', '')
            sum += 900 
        
    for c in roman_num: 
           sum += roman[c]

    return sum
 



