# sort elements of array in ascending and descending order
size=int(input("enter array size:"))
arr=[]
print("enter array elements:")
for i in range(0,size):
    element=int(input())
    arr.append(element)

print("array elements in ascending order:")
arr.sort()
print(arr)
print(*arr)    

print("array elements in descending order:")
arr.sort(reverse=True)
print(arr)
print(*arr)    
