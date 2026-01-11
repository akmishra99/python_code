# file amd_python_problem.py
# Author:- Alok Kumar Mishra
# e-mail:- akmishra_99@yahoo.com
# Date :- Jan 10,2026
#
#
#below is how to run this program on windows 11 using power shell (PS)
#
#PS C:\Users\akmis\Documents> python amd_python_problem.py
#1234567892/900,1234567893/950,1234567894/1000
#sample_key =  {'1234567892:1234567894': {'minimum': 900, 'maximum': 1000, 'average': 950.0}}
#{'1234567892:1234567894': {'minimum': 900, 'maximum': 1000, 'average': 950.0}}
#PS C:\Users\akmis\Documents>




def find_string(string_stream = "1234567890/800, 1234567891/850,1234567892/900,1234567893/950,1234567894/1000",start_and_stop_string  = "1234567892:1234567894" ):
    start_string ,stop_string = start_and_stop_string.split(":")
    filtered_string_streamList = []
    string_streamList = string_stream.split(",")
    i = 0
    found = False
    while i < len(string_streamList):
        if start_string in string_streamList[i]:
            filtered_string_streamList.append(string_streamList[i])
            found = True
        elif stop_string in string_streamList[i]:
            filtered_string_streamList.append(string_streamList[i])
            break
        elif found:
            filtered_string_streamList.append(string_streamList[i])

            
        
        i += 1

    
    return ','.join(filtered_string_streamList)

def get_statistics(string_stream = "1234567890/800, 1234567891/850,1234567892/900,1234567893/950,1234567894/1000" ,start_and_stop_string  = "1234567892:1234567894"):
    string_streamList = string_stream.split(",")
    list_in_consideration = []
    for i in range(len(string_streamList)):
        list_in_consideration.append(int(string_streamList[i].split("/")[1]))
    minimum = min(list_in_consideration)
    maximum = max(list_in_consideration)
    average = sum(list_in_consideration)/len(list_in_consideration)
    key_data = {}
    key_data["minimum"] = minimum
    key_data["maximum"] = maximum
    key_data["average"] = average

    sample_key = {}

    sample_key[start_and_stop_string] = key_data
    print("sample_key = ",sample_key)
    return sample_key

if __name__ == "__main__":
    sample_string = "1234567890/800, 1234567891/850,1234567892/900,1234567893/950,1234567894/1000"
    start_and_stop_string = "1234567892:1234567894"
    print(find_string(sample_string,start_and_stop_string))
    print(get_statistics(find_string(sample_string  ,start_and_stop_string),start_and_stop_string))

