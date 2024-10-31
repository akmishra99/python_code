#!/usr/bin/python3
"""
Author:- Alok Kumar Mishra
e-mail; akmishra_99@yahoo.com
Oct 29,2024

this file implements decorator with arguments , depending on how my_func is called it throws exception if input is '5' or '87" and prints success mesage by executing my_function when inpit is '1'

here is output of program

akmishra@windows11:~/scratch_oct_30_2024/malloc_copy_demo$ ./decorator_with_arguments.py
kwargs = {'5': 'MyCustomError', '87': 'bad_operands', '1': 'success', 'fourth': '4'}

MyCustomError = raising MyCustomError

kwargs = {'87': 'bad_operands'}

bad_operands  = raising bad_operands

kwargs = {'1': 'success'}

j = hello, k = there

key i = 1 and value = success

called2 = success

"""

class MyCustomError(Exception):
    def __init__(self, message="An error occurred MyCustomError occured:"):
        self.message = message
        super().__init__(self.message)

class bad_operands(Exception):
    def __init__(self, message="An error occurred bad_operands occured occured:"):
        self.message = message
        super().__init__(self.message)

def my_decoratror(j,k):
    def inner_function(func):
        def wrapper(*args,**kwargs):
            #print(kwargs)
            for key,value in kwargs.items():
                print("kwargs = %s\n" % kwargs)
                if key == "5":
                    raise MyCustomError("raising MyCustomError")
                elif key == "87":
                    raise bad_operands("raising bad_operands")
                elif key == "1":
                    print("j = %s, k = %s\n" % (j,k))
                    return func(*args,**kwargs)
        return wrapper
    return inner_function

@my_decoratror(j="hello",k="there")
def my_function(*args,**kwargs ):
    if kwargs is not None:
        for i ,value in kwargs.items():
            print("key i = %s and value = %s\n" % (i,value))
        return "success"
    else:
        return "failure"

if __name__=='__main__':
    given_input = {"5":"MyCustomError","87":"bad_operands","1":"success","fourth":"4"}
    given_input_success = {"1":"success" } 
    given_input_failure = {"87":"bad_operands"}
    try:
        called = my_function(**given_input  )
    except MyCustomError as e:
        print("MyCustomError = %s\n" % e)
    except bad_operands  as e:
        print("bad_operands  = %s\n" % e)
    else:
        print("called = %s\n" % called)

    try:
        called3 = my_function(**given_input_failure )
    except MyCustomError as e:
        print("MyCustomError = %s\n" % e)
    except bad_operands  as e:
        print("bad_operands  = %s\n" % e)
    else:
        print("called3= %s\n" % called3)



    try:
        called2 =  my_function(**given_input_success)
    except MyCustomError as e:
        print("MyCustomError = %s\n" % e)
    except bad_operands  as e:
        print("bad_operands  = %s\n" % e)
    else:
        print("called2 = %s\n" % called2)
