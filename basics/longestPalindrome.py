# find longest palindrome in an array
size=int(input("enter array size:"))
arr=[]
print("enter array elements:")
for i in range(0,size):
    element=int(input())
    arr.append(element)


arr.sort(reverse=True)

for item in arr:
    if str(item)==str(item)[::-1]:
        print("longest palindrome number is {}".format(item))
        break


