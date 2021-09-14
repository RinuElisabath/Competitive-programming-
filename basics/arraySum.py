# calculate sum of elements of an array
#sum can also be found using inbuit function sum(arr)
size=int(input("enter array size:"))
arr=[]
for i in range(0,size):
    element=int(input())
    arr.append(element)
sum=0    
for item in arr:
    sum=sum+item
print("sum is {}".format(sum))    

