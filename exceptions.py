# What Are Exceptions?
#Exceptions are events that disrupt the normal flow of a program. 
#They occur when an error is encountered during program execution. 
#Common exceptions include:

#ZeroDivisionError: Dividing by zero.
#FileNotFoundError: File not found.
#ValueError: Invalid value.
#TypeError: Invalid type.

try:
    a=int(input("Enter a number1"))
    b=int(input("Enter a number2"))
    c=a/b
    d=a*b
    e=a+b

except NameError as ex2:
    ## code for handling exception message
    print("NameError", ex2)
except TypeError as ex:
    ## code for handling exception message
    print("TypeError", ex)
except ZeroDivisionError as ex1:
    ## code for handling exception message
    print("ZeroDivisionError, Enter non zero value", ex1)
except Exception as ex3:
    ## code for handling exception message
    print("problem may have occured")

#if exception not caught in the exceptions
else:
    print("below because there was no exception")
    print(c)
    print(d)
    print(e)
#finally code block runs in case of exception or no exception
finally:
    print("user entered ", format(a))
    print("user entered ", format(b))
    print("This will be printed even if there is exception.")
    
