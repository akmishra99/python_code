#!/usr/bin/python3
"""
 this program opens file error.log reads lines and if line contains ERROR then it is written to file output.txt and if line
 does not contain then line is skipped


 here is sample error.log file


 more error.log
this line contains ERROR
this is simple line
akmishra@windows11:~/scratch_oct_15_2024$

here is how this program was run 
akmishra@windows11:~/scratch_oct_15_2024$ ./filter_lines.py
akmishra@windows11:~/scratch_oct_15_2024$

"""
def write_to_file_only_lines_which_contain_error():
    with open("output.txt",'w') as out:
        with open("error.log","r") as f:
            lines = f.readlines()
            for line in lines:
                if ( "ERROR" in line):
                    out.write(line)
                else:
      	            continue


if __name__=='__main__':
    write_to_file_only_lines_which_contain_error()
