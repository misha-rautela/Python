# Difference between iterator and generator
# to create an iterator we use iter() function
# to create a generator we use a function with yield keyword
# yield will save the local variable
# Generator uses the yield keyword.
# Gerator in python lets us write fast and compact code
# Iterator in python is memory efficient. 


lst=[1,2,3,4]
#iterator
iterable=iter(lst)
try:
    print(next(iterable))
except StopIteration as ex:
    print("iterator is at the end of list", ex)
except Exception as ex:
    print("iterator is at the end of list")

#Generator
def square1(n):
    for i in range(n):
        yield i**2

a=square1(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
try:
    num=int(input("Enter a range you want to iterate to get square value list"))
    a=square1(num)
    for i in range(num):
        print(next(a))
except Exception as ex:
    print("end of iterator")
