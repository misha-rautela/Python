#selection sort
#Time complexity O(n^2)
#Space complexity as n, as it requires to save min. 
arr=[50,38,45,79,19,27,25,39]
n=len(arr)
loc=0
for i in range(n-1):
    for j in range(i+1,n-1):
        if (arr[j]< arr[j+1]):
            loc=j
        else:
            loc=j+1
    arr[i],arr[loc]=arr[loc],arr[i]
    
print(arr)
