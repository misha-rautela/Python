#Lists
#Lists in Python are ordered, mutable sequences of items. They are versatile data structures used to store collections of elements, which can be of different data types.
#Lists are created using square brackets [], with elements separated by commas.

#Example list initialization
fruits=["apple","banana","cherry","kiwi","gauva"]
#append an element at the end
fruits.append("orange")
#insert an element at specific location
fruits.insert(1,"watermelon")
print(fruits)
## Remove the first occurance of an item
fruits.remove("banana") ## Removing the first occurance of an item
print(fruits)
#Pop/Remove the last element from the list
popped_fruits=fruits.pop()
print(popped_fruits)
print(fruits)
#to get the index of an element in the list
index=fruits.index("cherry")
print(index)
#to sort the list
fruits.sort()
print(fruits)

# Operations on an integer list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index,number in enumerate(numbers):
    print(index,number)

#to create a list of square within a range
lst=[]
for x in range(10):
    lst.append(x**2)

#Another way to do the same
square=[num**2 for num in range (10)]

# long way to create a list of even numebers
lst=[]
for i in range(10):
    if i%2==0:
        print("even number", i)
        lst.append(i)
    else:
        print("odd number", i)

print(lst)

# comprehensive to create a list of even numbers
even_number = [num for num in range(100) if(num%2==0)]

## Nested List Comphrension
lst1=[1,2,3,4]
lst2=['a','b','c','d']

pair=[[i,j] for i in lst1 for j in lst2 ]
print(pair)

## List Comprehension with function calls
words = ["hello", "world", "python", "list", "comprehension"]
lengths=[len(x) for x in words]
print(lengths)  # Output: [5, 5, 6, 4, 13]

# for loop to print the elements of list
inventory = ["apples", "bananas", "oranges", "grapes"]
for x in inventory:
    print(f"inventory is {x} is in the stock")
