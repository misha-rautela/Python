#Insertion Sort
#Best case scenario when it's incremental array 
# time complexity is order of n, i.e. O(n)
#worst case scenario:
# time complexity is order of n^2. O(n^2)
a=[70,90,100,99,85,55,101,110,71]
n=len(a)
for i in range(n-1):
    #print("i",i)
    if (a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
        j=i-1
        #print("j,",j)
        while j>=0:
            #print("j2",j)
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                j=j-1
            else:
                j=j-1

print("a",a) 
