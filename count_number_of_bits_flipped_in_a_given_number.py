



#file count_number_of_bits_flipped_in_a_given_number.py
#this program finds the number of bits flipped in a given number

#PS C:\Users\akmis\scratch_oct_29_2025> python.exe .\count_number_of_bits_flipped_in_a_given_number.py
#given_number in hex = 0xaaaa and total bits flipped in this  number = 16

#given_number in hex = 0x101 and total bits flipped in this  number = 3


def count_number_of_bits_flipped(given_number):
    temp = given_number
    temp2 = given_number
    bit_length = given_number.bit_length() 
    bit_flipped = 0
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

    return bits_flipped
if __name__=='__main__':
    given_number = 0xAAAA
    print("given_number in hex = 0x%x and total bits flipped in this  number = %d\n" % (given_number,count_number_of_bits_flipped(given_number)))
    given_number = 0x101
    print("given_number in hex = 0x%x and total bits flipped in this  number = %d\n" % (given_number,count_number_of_bits_flipped(given_number)))
            
             
