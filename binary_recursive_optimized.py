#!/usr/bin/python3
#
#	a program to do recursive binary search
#	C:\Users\akmis\scratch_dec_10_2024>python3 binary_recursive_optimized.py
#	False
#	True
#	True
#	False
#	True
#	True
#	True
#	True
#	False
def binary_search(arr = [ 1,2,3,4,5,6,8,9, 10] ,number_to_search = 7):
	mid = int (len(arr) /2)
#	if len(arr) == 2:
#		if number_to_search in arr:
#			return True
	if arr[mid] == number_to_search:
		return True 
	if mid == 0:
        	return False    


	if arr[mid] < number_to_search:
		arr = arr [mid:]
	elif arr[mid] > number_to_search:
		arr = arr[0:mid]
	return binary_search(arr , number_to_search)


if __name__=='__main__':
	print(binary_search())
	print(binary_search(number_to_search = 8))
	print(binary_search(number_to_search = 3))
	print(binary_search(number_to_search = 0))
	print(binary_search(number_to_search = 5))
	print(binary_search(number_to_search = 4))
	print(binary_search(number_to_search = 10))
	print(binary_search(number_to_search = 1))
	print(binary_search(number_to_search = 11))
