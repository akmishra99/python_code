#this is file nth_largest_element.py
# Author :- Alok Kumar Mishra (akmishra_99@yahoo.com)
# Date:- Oct 10,2025
# this program finds nth largest number in given list
# first argument to this porgram is list of integers or numbers 
# second argument is nth largest number in list
# Please see below how to invoke it 


#C:\Users\akmis\scratch_oct_10_2025>python nth_largest_element.py "[3,6,2,3,8,5,8,7]" 3
# 3largest element in given_list = ['3', '6', '2', '3', '8', '5', '8', '7'] is = 6


#C:\Users\akmis\scratch_oct_10_2025>python nth_largest_element.py  "3,6,2,3,8,5,8,7,9,19,11"
#  2nd largest element = 11  in given_list = ['3', '6', '2', '3', '8', '5', '8', '7', '9', '19', '11']

#C:\Users\akmis\scratch_oct_10_2025>python nth_largest_element.py
# 2nd largest element = 7 in given_list = [3, 6, 2, 3, 8, 5, 8, 7]

#C:\Users\akmis\scratch_oct_10_2025>python nth_largest_element.py "3,6,2,3,8,5,8,7,9,19,11" 10
#list index out of range
# 10th largest element in given_list = ['3', '6', '2', '3', '8', '5', '8', '7', '9', '19', '11'] is = None




import sys


def find_nth_largest_element_in_a_list(given_list =[3,6,2,3,8,5,8,7] ,nth_element  = 2):
    list_of_integers = list(map(int, given_list))
    try:
        return sorted(set(list_of_integers))[-nth_element]
    except IndexError as e:
        print(e)
    except Exception as f:
        print(f)
    


if __name__=='__main__':
    given_list = [3,6,2,3,8,5,8,7]
    nth_element = 2
    if len(sys.argv) == 3:
        given_list = sys.argv[1].strip('[').strip(']').split(',')
        nth_element = int(sys.argv[2])

        print(" %dth largest element in given_list = %s is = %s" % (nth_element,given_list,find_nth_largest_element_in_a_list(given_list,nth_element)))
    elif len(sys.argv) == 2:
        given_list = sys.argv[1].strip('[').strip(']').split(',')
        print("  2nd largest element = %d  in given_list = %s " % (find_nth_largest_element_in_a_list(given_list = given_list),given_list))
    else:
        print(" 2nd largest element = %d in given_list = %s" % (find_nth_largest_element_in_a_list(),given_list))
   