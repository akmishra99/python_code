#!/usr/bin/python3

#this python program finds duplicate numbers in a list
# it returns a list of tuples whose first element is number to serached for second element is number of times
# (count) element ocurrs
# here is output of program when run 
#C:\Users\akmis\scratch_dec_10_2024>python3 find_duplicate_numbers.py
#result =  [(1, 4), (2, 3), (3, 3), (4, 2)]

def find_duplicates_and_return_result_in_list_of_tuple (arr = [1,2,1,3,2,1,3,4,1,2,3,4]):
	count = 0 
	result = [] 
	number_already_processed = [] 
	for j in arr:
		if j not in number_already_processed:
			count = 0
			for i in range(len(arr) ):
				if arr[i] == j:
					count = count + 1  
			if count:
				a_tuple = (j,count)
				result.append(a_tuple)
				count = 0 
				number_already_processed.append(j)
	return result


if __name__=='__main__':
	print ( "result = ",find_duplicates_and_return_result_in_list_of_tuple())
