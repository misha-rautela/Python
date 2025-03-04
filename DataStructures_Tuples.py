#Tuples are a fundamental data structure in Python, representing ordered, immutable sequences of elements. Once a tuple is created, its elements cannot be modified, added, or removed. 
#This immutability makes tuples suitable for storing fixed collections of data. 
#The main difference between tuples and lists is mutability. Lists are mutable, allowing modification of their elements, while tuples are immutable. 
#Tuples are generally more memory-efficient and can be faster to process than lists in certain scenarios.

#Tuples are defined by enclosing a comma-separated sequence of elements within parentheses ().

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

mixed_tuple=(1,"Hello World",3.14, True)
numbers=tuple([1,2,3,4,5,6])
print(numbers.count(1))
print(numbers.index(3))

### Unpacking with *
first,*middle,last=numbers
print(first)
print(middle)
print(last)
