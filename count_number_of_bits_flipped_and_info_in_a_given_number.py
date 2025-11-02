#!C:\Python312\python.exe

#!/usr/bin/env python3



#file count_number_of_bits_flipped_and_info_in_a_given_number.py
#this program finds the number of bits flipped in a given number
# also gives statistics about given number 
# Author :- Alok Kumar Mishra
# e-mail : akmishra_99@yahoo.com
# Nov 1 ,2025

r""" PS C:\Users\akmis\scratch_oct_29_2025> python.exe count_number_of_bits_flipped_and_info_in_a_given_number.py
given_number in hex = 0xaaaa

given number = 43690
                number of zero bits flipped = 8
                number of one bits flipped = 8
                number of bits flipped in this number = 16
                number of zero bits = 9
                number of one bits = 8

given_number in hex = 0x101

given number = 257
                number of zero bits flipped = 1
                number of one bits flipped = 2
                number of bits flipped in this number = 3
                number of zero bits = 8
                number of one bits = 2

given_number in hex = 0xaaaaaaaa

given number = 2863311530
                number of zero bits flipped = 16
                number of one bits flipped = 16
                number of bits flipped in this number = 32
                number of zero bits = 17
                number of one bits = 16


on Raspberrypi compute module 5 
akmishra@raspberrypiCm5Bedroom4:~/scratch_nov_1_2025 $ python count_number_of_bits_flipped_and_info_in_a_given_number.py
given_number in hex = 0xaaaa

given number = 43690
                number of zero bits flipped = 8
                number of one bits flipped = 8
                number of bits flipped in this number = 16
                number of zero bits = 9
                number of one bits = 8

given_number in hex = 0x101

given number = 257
                number of zero bits flipped = 1
                number of one bits flipped = 2
                number of bits flipped in this number = 3
                number of zero bits = 8
                number of one bits = 2

given_number in hex = 0xaaaaaaaa

given number = 2863311530
                number of zero bits flipped = 16
                number of one bits flipped = 16
                number of bits flipped in this number = 32
                number of zero bits = 17
                number of one bits = 16

 """

class bit_info:
    def __init__(self,given_number):
        self.given_number = given_number
        self.number_of_zero_bits_flipped = 0
        self.bits_flipped = 0
        self.number_of_one_bits_flipped = 0
        self.number_of_zero_bits = 0
        self.number_of_one_bits = 0 
    def __str__(self):
        print("given number = %d" % self.given_number)
        print("\t\tnumber of zero bits flipped = %d" % self.number_of_zero_bits_flipped)
        print("\t\tnumber of one bits flipped = %d" % self.number_of_one_bits_flipped)
        print("\t\tnumber of bits flipped in this number = %d" % self.bits_flipped)    
        print("\t\tnumber of zero bits = %d" % self.number_of_zero_bits)
        print("\t\tnumber of one bits = %d" % self.number_of_one_bits)
        return ""

def count_number_of_bits_flipped(given_number):
    temp = given_number
    temp2 = given_number
    bit_length = given_number.bit_length() 
    
    number_of_zero_bits_flipped = 0
    bits_flipped = 0
    number_of_one_bits_flipped = 0
    previous_zero_bit = False
    previous_one_bit  = False
    number_of_zero_bits = 0
    number_of_one_bits = 0 
    for i in range(bit_length + 1): # range iterates from 0 to bit_lenght -1 ,so one is added 
        temp = temp2 & 0x1
        if temp:
            number_of_one_bits += 1
            previous_one_bit = True
            if previous_zero_bit:
                previous_zero_bit = False
                number_of_zero_bits_flipped  += 1
                bits_flipped += 1
        else:
             number_of_zero_bits += 1
             previous_zero_bit = True
             if previous_one_bit:
                 previous_one_bit = False
                 number_of_one_bits_flipped += 1
                 bits_flipped += 1

        temp2 = temp2 >> 1

    a_bit_info = bit_info(given_number)
    a_bit_info.number_of_zero_bits_flipped = number_of_zero_bits_flipped
    a_bit_info.bits_flipped = bits_flipped
    a_bit_info.number_of_one_bits_flipped = number_of_one_bits_flipped
    a_bit_info.number_of_zero_bits = number_of_zero_bits
    a_bit_info.number_of_one_bits = number_of_one_bits

    return a_bit_info





if __name__=='__main__':
    given_number = 0xAAAA
    print("given_number in hex = 0x%x\n" % (given_number))
    temp_number = count_number_of_bits_flipped(given_number) #

    print(temp_number)  #
    given_number = 0x101
    print("given_number in hex = 0x%x\n" % (given_number))
    temp_number = count_number_of_bits_flipped(given_number)
    print(temp_number)
    
    given_number = 0xAAAAAAAA
    print("given_number in hex = 0x%x\n" % (given_number))
    temp_number = count_number_of_bits_flipped(given_number)
    print(temp_number)
    
                
             
