#Sets are a built-in data type in Python used to store collections of unique items. 
#They are unordered, meaning that the elements do not follow a specific order, and they do not allow duplicate elements. Sets are useful for membership tests, eliminating duplicate entries, and performing mathematical set operations like union, intersection, difference, and symmetric difference.
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

### Union
union_set=set1.union(set2)
print(union_set)

## Intersection
intersection_set=set1.intersection(set2)
print(intersection_set)

set1.intersection_update(set2)
print(set1)

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
print(set1.difference(set2))
print(set2.difference(set1))

student={"name":"Misha","age":18,"grade":2025}
for key,value in student.items():
    print(key,value)

for key,value in student.items():
    print(f"key is {key} and values is {value}")

## set Comphrehension
squares=[x**2 for x in range(5)]
print(squares)

