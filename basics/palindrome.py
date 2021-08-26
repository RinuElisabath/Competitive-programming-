#check if given string is palindrome or not

str1=input("enter string:")
index=-1
flag=1
for i in range(len(str1)):
    if str1[i]==str1[index]:
        index-=1
    else:
        flag=0
        break
if flag==1:
    print("palindrome")
else:
    print("not a palindrome")     


'''
str1=input("enter string:")
str2=str1[-1::-1]
if str1==str2:
    print("palindrome")
else:
    print("not palindrome") 
'''    