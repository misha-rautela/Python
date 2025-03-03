# Bubble Sort 
#Time Complexity Order of n square O(n^2)
#Space Complexit constant 1, as no extra space is used
arr=[70,20,50,30,90,5,150,120]
n=len(arr)
for i in range(n-1):
    for j in range(0,n-i-1):
        if (arr[j]> arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
            
print(arr)
