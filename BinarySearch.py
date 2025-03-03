#Search for an element using Binarcy Search using recursion
#Time Complexity : O(n)
#Space Complexity : O(1)

def Binarysearch(i,j,x,arr):
    while i<=j:
        mid=i+(j-i)//2
        if(arr[mid]==x):
            #print("Searching element is present at the index", mid)
            return mid
        elif(arr[mid]>x):
            return Binarysearch(i,mid-1,x,arr)
        elif(arr[mid]<x):
            return Binarysearch(mid+1,j,x,arr)
        return -1
#Driver Code
print("Here's the array you want to search an integer arr=[2,4,8,12,20,22,50,70,110] \n")
x=int(input("Enter the element you want to search"))
arr=[2,4,8,12,20,22,50,70,110]
l=len(arr)-1
#Function Calling
result=Binarysearch(0,l,x,arr)
print("Searching element is present at the index", result)
