def merge_sort(a,l,h):
    if l<h:
        mid=(l+h)//2
        merge_sort(a,l,mid)
        merge_sort(a,mid+1,h)
        combine(a,l,mid,h)
def combine(a,l,mid,h):
    for i in range(l,h+1):
           temp[i]=a[i]
    i=l
    k=l
    j=mid+1
    while (i<=mid and j<=h):
        if(temp[i]<=temp[j]):
            a[k]=temp[i]
            i=i+1
            k=k+1
        else:
            a[k]=temp[j]
            j=j+1
            k=k+1
    while(j<=h):
       a[k]=temp[j]
       j=j+1
       k=k+1
    while i<=mid:
        a[k]=temp[i]
        i=i+1
        k=k+1
a=eval(input("enter the elements:"))
n=len(a)
temp=[0]*n
l=a[0]
h=a[n-1]
print("given array:",a)
merge_sort(a,0,n-1)
print("sorted array:",a)
