#perform binary search until low<=high coz when the element is not present in array , sometimes low becomes > high..tehn it should stop
#returns position ,not the index
#complexity : O(logn)

def binarysearch(list2,key,low,high):
    if(low<=high):
        mid=(low+high)//2
        if list2[mid]==key:
            return mid+1
        elif list2[mid]<key:
            return binarysearch(list2,key,mid+1,high)
        else:
            return binarysearch(list2,key,low,mid-1)
    else:
        return -1  


low=0
list1=[]
length=int(input("enter length:"))
print("enter items")
for i in range(0,length):
    list1.append(int(input()))
list2=sorted(list1)
print(list2)
high=length-1
key=int(input("enter item to be searched"))
print(binarysearch(list2,key,low,high)) 




      
    