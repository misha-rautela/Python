import random
import sys
import os
import petl

class calc:

	def add(a,b):
            return(a+b)
        def subtract(a,b):
            return(a-b)
        def multi(a,b):
            return(a*b)
        def divide(a,b):
            return(a/b)
i=1
result=1
while i < 3:
	x=input('Enter first number')
        y=input('Enter second number')
        z=str(raw_input("Enter the operator + - % * "))
        if(z == '*'):
	        print(calc.multi(x,y))                                                                                                                                                                                                               
        elif(z == '+'):
            result = calc.add(x,y)
        elif(z == '/'):
            result = calc.divide(x,y)
        elif(z == '-'):
            result = calc.subtract(x,y)
        else:
            inp=str(raw_input("You have not entered a correct operator sweets!! Wanna try again? Answer in YES or NO"))
            if(inp == 'YES'):
                i = i + 1
                continue
            elif(inp == 'NO'):
                break
            else:
                print("You had your chances sweets, too bad! Ta Ta!! ")
        print(result)
        break
