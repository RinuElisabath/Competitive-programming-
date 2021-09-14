# find smallest element in array
size=int(input("enter array size:"))
arr=[]
print("enter array elements:")
for i in range(0,size):
    element=int(input())
    arr.append(element)
print("smallest element is {}".format(min(arr)))    