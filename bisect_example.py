import os
import sys
import bisect as b
def f_index(a, x):
    i = b.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = b.bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = b.bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = b.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = b.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError
Array1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print Array1
a = f_index(Array1,2)
print(a)
print(f_index(Array1,2))
print(find_lt(Array1,2))
print(find_le(Array1,2))
print(find_gt(Array1,2))
print(find_ge(Array1,2))
