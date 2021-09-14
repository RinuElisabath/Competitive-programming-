# print the reversed array
size=int(input("enter array size:"))
arr=[]
print("enter array elements:")
for i in range(0,size):
    element=int(input())
    arr.append(element)

print("reversed array is ",*arr[::-1])    