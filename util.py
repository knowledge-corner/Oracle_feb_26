# This is utility module file which project specific utility functions - 
'''
Problem Statement - 
1. Validate the arguments passed to the functions
2. All the functions has similar structure and validations requirements
3. More similar functions are expected to be added in future by different developers, 
so we need to maintain a standard validation structure across all the functions in the module to maintain the code quality and readability.
4. Another module is expected to be created which might need to use same validation structure

Decorators - 
- A design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. 
- Decorators are usually called before the definition of a function you want to decorate.
- They use the concept of inner and outer functions, where the outer function takes a function as an argument 
- The inner function performs the additional functionality and then calls the original function, returning its result.
'''

def decot(func_obj) :
    def inner():
        print("This is the inner function")
        return func_obj()   # inner function returns call to the original function passed as an argument to the outer function
    return inner

@decot   # decorator is applied to the function func
def func():
    print("This is the original function")



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(n, 1, -1):
            fact *= i
        return fact

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def addition(a, b):
    return a + b