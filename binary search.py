def binary_search(l,h,key):
    while l<=h:
        mid=(l+h)//2
        if(a[mid]==key):
            return 1
        elif(a[mid]<key):
            l=mid+1
            binary_search(l,h,key)
        elif(a[mid]>key):
            h=mid-1
            binary_search(l,h,key)
        else:
            return -1
a=eval(input("enter the array of element:"))
l=0
h=len(a)-1
key=eval(input("enter the number:"))
print(binary_search(l,h,key))
