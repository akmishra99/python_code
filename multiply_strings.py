#!/usr/bin/python
import sys

#write a method take input of strings and implement the Multiply strings.
#Example:
#Input: num1 = "2", num2 = "3"  
#Output: "6"
#
# 
#C:\Users\akmis\scratch_june_3_2026>python3 multiply_strings.py
#multiplication of string one and string two is = 121
# Author:- Alok Kumar Mishra
# e-mail : akmishra_99@yahoo.com
# Date:- June 3 ,2026
#
r""" 
Please not strings containg with floating point numbers are not considered as valid input.
 Only strings with valid integers are considered as valid input. 
C:\Users\akmis\scratch_june_4_2026>python3 multiply_strings.py
usage string1 and string2 multiply_strings.py

multiplication of string one and string two is = 121


C:\Users\akmis\scratch_june_4_2026>python3 multiply_strings.py 100 10
multiplication of string one and string two is = 1000

multiplication of two strings = 1000


C:\Users\akmis\scratch_june_4_2026>python3 multiply_strings.py 100 105
multiplication of string one and string two is = 10500

multiplication of two strings = 10500


C:\Users\akmis\scratch_june_4_2026>python3 multiply_strings.py 123 123
multiplication of string one and string two is = 15129

multiplication of two strings = 15129


C:\Users\akmis\scratch_june_4_2026> vi multiply_strings.py

C:\Users\akmis\scratch_june_4_2026>C:\Users\akmis\scratch_june_4_2026>python3 multiply_strings.py
usage string1 and string2 multiply_strings.py

multiplication of string one and string two is = 121


C:\Users\akmis\scratch_june_4_2026>python3 multiply_strings.py 100 10
multiplication of string one and string two is = 1000

multiplication of two strings = 1000


C:\Users\akmis\scratch_june_4_2026>python3 multiply_strings.py 100 105
multiplication of string one and string two is = 10500

multiplication of two strings = 10500


C:\Users\akmis\scratch_june_4_2026>python3 multiply_strings.py 123 123
multiplication of string one and string two is = 15129

multiplication of two strings = 15129



C:\Users\akmis\scratch_june_4_2026>
PS C:\Users\akmis\scratch_june_4_2026> python .\multiply_strings.py "-100" 20
multiplication of string one and string two is = -2000

multiplication of two strings = -2000

PS C:\Users\akmis\scratch_june_4_2026> python .\multiply_strings.py "-100" "-20"
multiplication of string one and string two is = 2000

multiplication of two strings = 2000

"""

def is_float(given_string):
    if given_string.count('.') == 1:
        
        try:
            val = float(given_string)
            return val
        except ValueError:
            return False
    return False


def atoi(given_string):
    if (is_float(given_string)):
        print("floating point numbers are not considered as valid input\n")
        return 0
    list_of_numbers = list(given_string)
    valid_numbers = ['0','1','2','3','4','5','6','7','8','9']
    number = 0;
    k = 0
    list_of_numbers.reverse()
    for i in list_of_numbers:
        if i in valid_numbers:
                number += (10 ** k ) * int(i)
                k += 1
    # check if the first character is negative sign then make the number negative             
    if (list_of_numbers[-1] == '-'):
        number *= -1    
    return number 
            


def multiply(given_string, given_string_two):
    number1 = atoi(given_string)
    number2 = atoi(given_string_two)
    return_string = str(number1 * number2)
    print ("multiplication of string one = %s and string two = %s is equal to =  %s\n" % (given_string, given_string_two, return_string))
    
    return return_string
    
if __name__=="__main__":
    if ( (len(sys.argv ) <= 2) or  (len(sys.argv) > 3)):
        print("usage %s string1 and string2" %sys.argv[0])
        print("for example multiplication of string one and string two is = 121\n")
        multiply("11","11")
    else:
        print("multiplication of two strings = %s\n" % multiply(sys.argv[1],sys.argv[2]))

    
    
