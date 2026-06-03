#!/usr/bin/python

#write a method take input of strings and implement the Multiply strings.
#Example:
#Input: num1 = "2", num2 = "3"  
#Output: "6"
#
# 
#C:\Users\akmis\scratch_june_3_2026>python3 multiply_strings.py
#multiplication of string one and string two is = 121
#
def atoi(given_string):
    list_of_numbers = list(given_string)
    valid_numbers = ['0','1','2','3','4','5','6','7','8','9']
    number = 0;
    k = 0
    list_of_numbers.reverse()
    for i in list_of_numbers:
        if i in valid_numbers:
            if ( k == 0):
                k += 1
                number = int(i)
            else:
                number += 10 * int(i)
                   
                   
    return number 
            


def multiply(given_string, given_string_two):
    number1 = atoi(given_string)
    number2 = atoi(given_string_two)
    return_string = str(number1 * number2)
    print ("multiplication of string one and string two is = %s\n" % return_string)
    
    return return_string
    
if __name__=="__main__":
    multiply("11","11")
    
    
