# Dictionary is a built-in data type that stores data in key-value pairs. 
# Dictionary is unordered, mutable collection.
# Dictionaries are defined using curly braces {}, with key-value pairs separated by colons :. 
# Dictionary Keys must be immutable types (e.g., strings, numbers, tuples), while values can be of any type. 
# Dictionaries cannot have two items with the same key:

## Dictionary Comphrehension
squares={x:x**2 for x in range(5)}
print(squares)
## Dictionary Comphrehension
squares={x:x**2 for x in range(20) if (x%2==0)}
print(squares)


## Merge 2 dictionaries into one

dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
merged_dict={**dict1,**dict2}
print(merged_dict)

## Use a dictionary to count the frequency of elements in list

numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}

for i in numbers:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)


