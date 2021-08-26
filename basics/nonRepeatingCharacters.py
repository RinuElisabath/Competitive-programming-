#find non repeating characters in a string

str1=input("enter string:")
for i in str1:
    if str1.count(i)==1:
        print(i)