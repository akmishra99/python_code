#!/usr/bin/python3
def write_to_file_only_lines_which_contain_error():
    with open("output.txt",'w') as out:
        with open("error.log","r") as f:
            out.writelines(  line  for line in f.readlines() if "ERROR" in line  )

if __name__=='__main__':

    write_to_file_only_lines_which_contain_error()
