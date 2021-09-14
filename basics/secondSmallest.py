# find second smallest element in array
size=int(input("enter array size:"))
arr=[]
print("enter array elements:")
for i in range(0,size):
    element=int(input())
    arr.append(element)

arr.sort()

for i in range(1,size):
    if(arr[0]!=arr[i]):
        print("second smallest element is {}".format(arr[i]))  
        break  